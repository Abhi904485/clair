from django.contrib import admin
from django.utils.html import format_html
from django_admin_search.admin import AdvancedSearchAdmin

from clair.export import ExportCsvMixin, ExportPdfMixin
from .forms import FeatureSearchForm
from .models import Feature


# Register your models here.


@admin.register(Feature)
class FeatureAdmin(AdvancedSearchAdmin, ExportCsvMixin, ExportPdfMixin):

    def namespace_link(self):
        return format_html(
            '<a href="/{app_name}/{db_table}/{db_table_primary_key}/change/">{db_table_field}</a>'.format(
                app_name=self.namespace._meta.app_label, db_table=self.namespace._meta.db_table,
                db_table_primary_key=self.namespace.id, db_table_field=self.namespace.name))

    namespace_link.short_description = "Namespace Name"
    namespace_link.admin_order_field = "namespace"

    def version_format_link(self):
        return format_html(
            '<a href="/{app_name}/{db_table}/{db_table_primary_key}/change/">{db_table_field}</a>'.format(
                app_name=self.namespace._meta.app_label, db_table=self.namespace._meta.db_table,
                db_table_primary_key=self.namespace.id, db_table_field=self.namespace.version_format))

    version_format_link.short_description = "Namespace Version Format"
    version_format_link.admin_order_field = "namespace__version_format"
    list_display = ("id", "name", namespace_link, version_format_link, 'get_vulnerability_fixedin_feature_version',
                    'get_vulnerability_link')
    raw_id_fields = ("namespace",)
    search_fields = (
        "id", 'name', 'namespace__name', 'namespace__version_format', 'vulnerabilityfixedinfeature__version',
        'vulnerabilityfixedinfeature__vulnerability__name')
    ordering = ('name', "id")
    list_per_page = 5
    list_filter = ('namespace__version_format', 'namespace__name',)
    list_display_links = ("name", namespace_link, version_format_link, "id")
    actions = ["export_as_csv", "export_as_pdf"]
    search_form = FeatureSearchForm


    # def search_version_format(self, field, field_value, form_field, request, advanced_search_fields):
    #     if self.get_field_value(field):
    #         field_name = form_field.widget.attrs.get('filter_field', field)
    #         field_filter = field_name + form_field.widget.attrs.get('filter_method', '')
    #         return Q(**{field_filter: field_value})
    #
    # def search_id(self, field, field_value, form_field, request, advanced_search_fields):
    #     if self.get_field_value(field):
    #         field_name = form_field.widget.attrs.get('filter_field', field)
    #         field_filter = field_name + form_field.widget.attrs.get('filter_method', '')
    #         return Q(**{field_filter: field_value})
