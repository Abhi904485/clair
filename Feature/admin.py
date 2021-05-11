from django.contrib import admin
from django_admin_search.admin import AdvancedSearchAdmin

from clair.export import ExportCsvMixin, ExportPdfMixin
from clair.utility import get_link
from .forms import FeatureSearchForm
from .models import Feature


# Register your models here.


@admin.register(Feature)
class FeatureAdmin(AdvancedSearchAdmin, ExportCsvMixin, ExportPdfMixin):

    def namespace_link(self):
        tables = ['namespace', ]
        return get_link(self, 'name', tables)

    namespace_link.short_description = "Namespace Name"
    namespace_link.admin_order_field = "namespace"

    def version_format_link(self):
        tables = ['namespace', ]
        return get_link(self, 'version_format', tables)

    version_format_link.short_description = "Namespace Version Format"
    version_format_link.admin_order_field = "namespace__version_format"
    list_display = ("id", "name", namespace_link, version_format_link)
    raw_id_fields = ("namespace",)
    search_fields = ("id", 'name', 'namespace__name', 'namespace__version_format', 'vulnerabilityfixedinfeature__version', 'vulnerabilityfixedinfeature__vulnerability__name')
    ordering = ('name', "id")
    list_per_page = 20
    list_filter = ('namespace__version_format', 'namespace__name',)
    list_display_links = ("name", namespace_link, version_format_link, "id")
    actions = ["export_as_csv", "export_as_pdf"]
    search_form = FeatureSearchForm
