# -*- coding: utf-8 -*-
import sqlparse
from django.contrib import messages
from django.contrib.admin import ModelAdmin
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from django_admin_search import utils
from django_admin_search.forms import OverrideSearchForm


class AdvancedSearchAdmin(ModelAdmin):
    """
        class to add custom filters in django admin
    """
    change_list_template = 'admin/custom_change_list.html'
    advanced_search_fields = {}
    search_form_data = None
    search_form = OverrideSearchForm

    def get_queryset(self, request):
        """
            override django admin 'get_queryset'
        """
        query = None
        queryset = super().get_queryset(request)
        try:
            query = self.advanced_search_query(request)
            result_queryset = queryset.filter(query)
            if not result_queryset.exists():
                if not getattr(messages.get_messages(request), '_queued_messages', False):
                    messages.add_message(request, messages.INFO, 'No match Found', extra_tags='cvs')
                    messages.add_message(request, messages.INFO, 'Custom Filtered Query : {}'.format(str(result_queryset.query)), extra_tags='cvs')
                else:
                    pass
                return queryset
            else:
                return result_queryset
        except Exception as e:
            if not getattr(messages.get_messages(request), '_queued_messages', False):
                messages.add_message(request, messages.ERROR, 'falling back to select * from {}'.format(queryset.model._meta.app_label), extra_tags='cvs error')
                if query:
                    messages.add_message(request, messages.ERROR, '{} where {}'.format(queryset.query, query), extra_tags='cvs error')
                for err in e.args:
                    messages.add_message(request, messages.ERROR, '{} input is not properly formatted'.format(err), extra_tags='cvs error')
                    messages.add_message(request, messages.ERROR, 'input is not properly formatted as expected', extra_tags='cvs error')
            else:
                pass
            return queryset

    # def populate_search_form_from_url(self, request):
    #     populate_dict = {}
    #     for param in request.environ['QUERY_STRING'].split("&"):
    #         if param:
    #             k, v = param.split("=")
    #             if not k == "o":
    #                 populate_dict[k] = v
    #     if populate_dict:
    #         for k1, v1 in populate_dict.items():
    #             self.search_form.declared_fields[k1].widget.attrs['value'] = v1
    #     else:
    #         for k1, _ in populate_dict.items():
    #             self.search_form.declared_fields[k1].widget.attrs['value'] = ""

    def changelist_view(self, request, extra_context=None):
        self.advanced_search_fields = {}
        self.search_form_data = self.search_form(request.GET)
        # self.populate_search_form_from_url(request)
        self.extract_advanced_search_terms(request.GET)
        extra_context = {'asf': self.search_form_data}
        return super().changelist_view(request, extra_context=extra_context)

    def extract_advanced_search_terms(self, request):
        request._mutable = True  # pylint: disable=W0212

        if self.search_form_data is not None:
            for key in self.search_form_data.fields.keys():
                temp = request.pop(key, None)
                if temp:  # there is a field but it's empty so it's useless
                    if isinstance(temp, list) and temp[0] !="":
                        self.advanced_search_fields[key] = temp

        request._mutable = False  # pylint: disable=W0212

    def get_field_value(self, field):
        """
            check if field has value passed on request
        """
        if field in self.advanced_search_fields:
            return True, self.advanced_search_fields[field][0]

        return False, None

    def get_field_value_override(self, field, field_value, form_field, request):
        """
            allow to override default field query
        """
        if hasattr(self, ('search_' + field)):
            return getattr(self, 'search_' + field)(field, field_value, form_field, request,
                                                    self.advanced_search_fields)
        return Q()

    @staticmethod
    def get_field_value_default(field, form_field, field_value, has_field_value, request):
        """
            mount default field value
        """
        if has_field_value:
            field_name = form_field.widget.attrs.get('filter_field', field)
            field_filter = field_name + form_field.widget.attrs.get('filter_method', '')

            try:
                field_value = utils.format_data(form_field, field_value)  # format by field type
                return Q(**{field_filter: field_value})
            except ValidationError:
                messages.add_message(request, messages.ERROR, _(f"Filter in field `{field_name}` "
                                                                "ignored, because value "
                                                                f"`{field_value}` isn't valid"))
            except Exception:
                messages.add_message(request, messages.ERROR, _(f"Filter in field `{field_name}` "
                                                                "ignored, error has occurred."))

        return Q()

    def advanced_search_query(self, request):
        """
            Get form and mount filter query if form is not none
        """
        query = Q()

        if self.search_form_data is None:
            return query

        for field, form_field in self.search_form_data.fields.items():
            has_field_value, field_value = self.get_field_value(field)

            if hasattr(self, ('search_' + field)):
                query &= self.get_field_value_override(field, field_value, form_field, request)
            else:
                query &= self.get_field_value_default(field, form_field, field_value, has_field_value, request)

        return query
