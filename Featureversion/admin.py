from django.contrib import admin
from django_admin_search.admin import AdvancedSearchAdmin

from clair.export import ExportCsvMixin, ExportPdfMixin
from clair.utility import get_link, custom_titled_filter
from .forms import FeatureVersionSearchForm
from .models import Featureversion


# Register your models here.


@admin.register(Featureversion)
class FeatureversionAdmin(AdvancedSearchAdmin, ExportCsvMixin, ExportPdfMixin):
    def feature_link(self):
        tables = ['feature', ]
        return get_link(self, 'name', tables)

    feature_link.short_description = "Feature Name"
    feature_link.admin_order_field = "feature"

    def namespace_link(self):
        tables = ['feature', 'namespace', ]
        return get_link(self, 'name', tables)

    namespace_link.short_description = "Namespace Name"
    namespace_link.admin_order_field = "feature__namespace__name"

    list_display = ("id", feature_link, "version", namespace_link)
    raw_id_fields = ("feature",)
    search_fields = ("id", "feature__name", "version", "id")
    ordering = ("version", "id")
    list_per_page = 20
    list_filter = (('version', custom_titled_filter("Feature Version")),
                   ('feature__namespace__name', custom_titled_filter("Namespace")))
    list_display_links = (feature_link, "version", "id", namespace_link)
    actions = ["export_as_csv", "export_as_pdf"]
    search_form = FeatureVersionSearchForm
