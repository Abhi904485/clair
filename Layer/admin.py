from datetime import datetime

import pytz
from django.contrib import admin, messages
from django.db import models
from django.db.models import Q
from django.forms import TextInput
from django.utils.html import format_html
from django_admin_search.admin import AdvancedSearchAdmin

from clair.export import ExportCsvMixin, ExportPdfMixin
from .forms import LayerSearchForm
from .models import Layer


# Register your models here.


@admin.register(Layer)
class LayerAdmin(AdvancedSearchAdmin, ExportCsvMixin, ExportPdfMixin):
    def namespace_link(self):
        return format_html(
            '<a href="/{app_name}/{db_table}/{db_table_primary_key}/change/">{db_table_field}</a>'.format(
                app_name=self.namespace._meta.app_label, db_table=self.namespace._meta.db_table,
                db_table_primary_key=self.namespace.id, db_table_field=self.namespace.name))

    namespace_link.short_description = "Namespace Name"
    namespace_link.admin_order_field = "namespace"

    def parent_link(self):
        if self.parent is None:
            app_name = self._meta.app_label
            db_table = self._meta.db_table
            db_table_primary_key = self.id
            db_table_field = "-"
        else:
            app_name = self.parent._meta.app_label
            db_table = self.parent._meta.db_table
            db_table_primary_key = self.parent.id
            db_table_field = self.parent.name
        return format_html(
            '<a href="/{app_name}/{db_table}/{db_table_primary_key}/change/">{db_table_field}</a>'.format(
                app_name=app_name, db_table=db_table,
                db_table_primary_key=db_table_primary_key, db_table_field=db_table_field))

    parent_link.short_description = "Layer Parent"
    parent_link.admin_order_field = "parent"

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': 150})},
    }
    list_display = ("id", 'name', parent_link, namespace_link,)
    raw_id_fields = ("namespace", "parent")
    search_fields = ("id", 'name', 'parent__name', 'namespace__name',)
    ordering = ("id", 'name',)
    list_filter = ('namespace',)
    list_per_page = 20
    list_display_links = ("id", 'name', parent_link, namespace_link,)
    actions = ["export_as_csv", "export_as_pdf"]
    search_form = LayerSearchForm

    @staticmethod
    def get_date_time(sd=None, st=None, ed=None, et=None):
        first_date_time = None
        second_date_time = None
        if sd and st:
            first_date_time = datetime.strptime(sd + st, "%Y-%m-%d%H:%M:%S").replace(tzinfo=pytz.UTC)
        if ed and et:
            second_date_time = datetime.strptime(ed + et, "%Y-%m-%d%H:%M:%S").replace(tzinfo=pytz.UTC)
        return first_date_time, second_date_time

    @staticmethod
    def get_field_name_and_field_filter(form_field, field):
        return form_field.widget.attrs.get('filter_field', field) + form_field.widget.attrs.get('filter_method', '')

    @staticmethod
    def split_field_value(field_value):
        if field_value:
            return field_value.split(" "), len(field_value.split(" "))
        return None

    def search_created_layer_between_date_time(self, field, field_value, form_field, request, advanced_search_fields):
        if self.get_field_value(field):
            if self.split_field_value(field_value):
                ((sd, st, ed, et), length) = self.split_field_value(field_value)
                if length == 4:
                    start_date_time, end_date_time = self.get_date_time(sd, st, ed, et)
                    return Q(**{self.get_field_name_and_field_filter(form_field, field): [start_date_time, end_date_time]})
                else:
                    messages.add_message(request, messages.ERROR,
                                         'Both Date time should be in yyyy-mm-dd HH:MM:SS with space separated Hours should be in 24 format')
                    return None
            else:
                return Q()

    def before_exact_after(self, field, field_value, form_field, request, advanced_search_fields):
        if self.get_field_value(field)[0]:
            if self.split_field_value(field_value):
                ((sd, st), length) = self.split_field_value(field_value)
                if length == 2:
                    start_date_time, _ = self.get_date_time(sd, st)
                    return Q(**{self.get_field_name_and_field_filter(form_field, field): start_date_time})
                else:
                    messages.add_message(request, messages.ERROR,
                                         'Date time should be in yyyy-mm-dd HH:MM:SS Hours should be in 24 format')
                    return None
        else:
            return Q()

    def search_created_on_or_before_date_time(self, field, field_value, form_field, request, advanced_search_fields):
        return self.before_exact_after(field, field_value, form_field, request, advanced_search_fields)

    def search_created_on_or_after_date_time(self, field, field_value, form_field, request, advanced_search_fields):
        return self.before_exact_after(field, field_value, form_field, request, advanced_search_fields)

    def search_created_on_exact_date_time(self, field, field_value, form_field, request, advanced_search_fields):
        return self.before_exact_after(field, field_value, form_field, request, advanced_search_fields)

    @staticmethod
    def get_query(field_value, form_field, field):
        year = False
        month = False
        day = False
        if len(field_value.split("-")) == 3:
            year, month, day = True, True, True
        elif len(field_value.split("-")) == 2:
            u1, u2 = field_value.split("-")
            if len(u1) == 4:
                year, month = True, True
            if len(u1) == 2:
                month, day = True, True
        elif len(field_value.split("-")) == 1:
            u1 = field_value.split("-")[0]
            if u1.endswith("y"):
                year = True
            elif u1.endswith("m"):
                month = True
            elif u1.endswith("d"):
                day = True
        format = ""
        methods = form_field.widget.attrs.get('filter_method', '')
        ymv, momv, dmv = methods.split(" ")
        filter_field = form_field.widget.attrs.get('filter_field', field)
        final_dict = {}
        if year and month and day:
            format += "-".join(["%Y", "%m", "%d"])
            derived_date = datetime.strptime(field_value, format)
            final_dict[filter_field + ymv] = derived_date.year
            final_dict[filter_field + momv] = derived_date.month
            final_dict[filter_field + dmv] = derived_date.day
        elif year and month:
            format += "-".join(["%Y", "%m"])
            derived_date = datetime.strptime(field_value, format)
            final_dict[filter_field + ymv] = derived_date.year
            final_dict[filter_field + momv] = derived_date.month
        elif month and day:
            format += "-".join(["%m", "%d"])
            derived_date = datetime.strptime(field_value, format)
            final_dict[filter_field + momv] = derived_date.month
            final_dict[filter_field + dmv] = derived_date.day
        elif year:
            format += "%Y"
            derived_date = datetime.strptime(field_value.rstrip("y"), format)
            final_dict[filter_field + ymv] = derived_date.year
        elif month:
            format += "%m"
            derived_date = datetime.strptime(field_value.rstrip("m"), format)
            final_dict[filter_field + momv] = derived_date.month
        elif day:
            format += "%d"
            derived_date = datetime.strptime(field_value.rstrip("d"), format)
            final_dict[filter_field + dmv] = derived_date.day
        return final_dict

    def search_created_on_day_month_year_and_or(self, field, field_value, form_field, request, advanced_search_fields):
        if self.get_field_value(field)[0]:
            return Q(**self.get_query(field_value, form_field, field))
        else:
            return Q()

    def search_parent_is_null(self, field, field_value, form_field, request, advanced_search_fields):
        if self.get_field_value(field)[0]:
            field_name = form_field.widget.attrs.get('filter_field', field)
            field_filter = field_name + form_field.widget.attrs.get('filter_method', '')
            if field_value.lower() == "true":
                field_value = True
                return Q(**{field_filter: bool(field_value)})
            elif field_value.lower() == "false":
                field_value = False
                return Q(**{field_filter: bool(field_value)})
            else:
                messages.add_message(request, messages.ERROR, "Input Should be True or false (Not Case Sensitive)")
                return None
        else:
            return Q()
