from django.contrib import admin
from django.db import models
from django.forms import TextInput
from django_admin_search.admin import AdvancedSearchAdmin
from rangefilter.filters import DateTimeRangeFilter

from clair.export import ExportCsvMixin, ExportPdfMixin
from clair.utility import is_null, day_month_year_and_or, get_link, \
    generate_query_for_date
from .forms import LayerSearchForm
from .models import Layer


# Register your models here.


@admin.register(Layer)
class LayerAdmin(AdvancedSearchAdmin, ExportCsvMixin, ExportPdfMixin):
    def namespace_link(self):
        tables = ['namespace']
        return get_link(self, 'name', tables)

    namespace_link.short_description = "Namespace Name"
    namespace_link.admin_order_field = "namespace"

    def parent_link(self):
        tables = ['parent']
        return get_link(self, 'name', tables)

    parent_link.short_description = "Layer Parent"
    parent_link.admin_order_field = "parent"

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': 150})},
    }
    list_display = ("id", 'created_at', namespace_link, 'name', parent_link, )
    raw_id_fields = ("namespace", "parent")
    search_fields = ("id", 'name', 'parent__name', 'namespace__name',)
    ordering = ("id", 'name',)
    list_filter = (('created_at', DateTimeRangeFilter), 'namespace')
    list_per_page = 20
    list_display_links = ("id", 'name', parent_link, namespace_link, 'created_at')
    actions = ["export_as_csv", "export_as_pdf"]
    search_form = LayerSearchForm

    def search_created_layer_between_date(self, field, field_value, form_field, request, advanced_search_fields):
        field_value = self.get_field_value(field)[1].strip() if self.get_field_value(field)[1] else self.get_field_value(field)[1]
        return generate_query_for_date(field, field_value, form_field, request, advanced_search_fields)

    def search_created_before_date(self, field, field_value, form_field, request, advanced_search_fields):
        field_value = self.get_field_value(field)[1].strip() if self.get_field_value(field)[1] else self.get_field_value(field)[1]
        return generate_query_for_date(field, field_value, form_field, request, advanced_search_fields)

    def search_created_after_date(self, field, field_value, form_field, request, advanced_search_fields):
        field_value = self.get_field_value(field)[1].strip() if self.get_field_value(field)[1] else self.get_field_value(field)[1]
        return generate_query_for_date(field, field_value, form_field, request, advanced_search_fields)

    def search_created_on_exact_date(self, field, field_value, form_field, request, advanced_search_fields):
        field_value = self.get_field_value(field)[1].strip() if self.get_field_value(field)[1] else self.get_field_value(field)[1]
        return generate_query_for_date(field, field_value, form_field, request, advanced_search_fields)

    def search_created_on_year_month_day_hour_minute_second_and_or(self, field, field_value, form_field, request, advanced_search_fields):
        field_value = self.get_field_value(field)[1].strip() if self.get_field_value(field)[1] else self.get_field_value(field)[1]
        return day_month_year_and_or(field, field_value, form_field, request, advanced_search_fields)

    def search_parent_is_null(self, field, field_value, form_field, request, advanced_search_fields):
        field_value = self.get_field_value(field)[1].strip() if self.get_field_value(field)[1] else self.get_field_value(field)[1]
        return is_null(field, field_value, form_field, request, advanced_search_fields)
