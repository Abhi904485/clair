from django.contrib import admin
from django_admin_search.admin import AdvancedSearchAdmin

from clair.export import ExportCsvMixin, ExportPdfMixin
from clair.utility import get_link
from .forms import LayerDiffFeatureVersionForm
from .models import LayerDiffFeatureversion


# Register your models here.


@admin.register(LayerDiffFeatureversion)
class LayerDiffFeatureversionAdmin(AdvancedSearchAdmin, ExportCsvMixin, ExportPdfMixin):

    def layer_link(self):
        tables = ['layer', ]
        return get_link(self, 'name', tables)

    layer_link.short_description = "Layer"
    layer_link.admin_order_field = "layer"

    def featureversion_link(self):
        tables = ['featureversion', ]
        return get_link(self, 'version', tables)

    featureversion_link.short_description = "Feature Version"
    featureversion_link.admin_order_field = "featureversion"

    list_display = ("id", layer_link, featureversion_link, 'modification')
    raw_id_fields = ('layer', 'featureversion')
    search_fields = ("id", 'layer__name', 'featureversion__version', 'modification')
    ordering = ("id", 'modification',)
    list_per_page = 20
    list_filter = ('modification', 'layer__namespace', 'featureversion',)
    list_display_links = ("id", layer_link, featureversion_link, 'modification')
    actions = ["export_as_csv", "export_as_pdf"]
    search_form = LayerDiffFeatureVersionForm
