from django.contrib import admin
from django.utils.html import format_html

from .models import LayerDiffFeatureversion


# Register your models here.


@admin.register(LayerDiffFeatureversion)
class LayerDiffFeatureversionAdmin(admin.ModelAdmin):

    def layer_link(self):
        return format_html(
            '<a href="/{app_name}/{db_table}/{db_table_primary_key}/change/">{db_table_field}</a>'.format(
                app_name=self.layer._meta.app_label, db_table=self.layer._meta.db_table,
                db_table_primary_key=self.layer.id, db_table_field=self.layer.name))

    layer_link.short_description = "Layer"
    layer_link.admin_order_field = "layer"

    def featureversion_link(self):
        return format_html(
            '<a href="/{app_name}/{db_table}/{db_table_primary_key}/change/">{db_table_field}</a>'.format(
                app_name=self.featureversion._meta.app_label, db_table=self.featureversion._meta.db_table,
                db_table_primary_key=self.featureversion.id, db_table_field=self.featureversion.version))

    featureversion_link.short_description = "Feature Version"
    featureversion_link.admin_order_field = "featureversion"

    list_display = (layer_link, featureversion_link, 'modification')
    readonly_fields = ('layer', 'featureversion')
    search_fields = ('layer__name', 'featureversion__version', 'modification')
    ordering = ('modification',)
    list_per_page = 20
    list_filter = ('modification', 'layer__namespace', 'featureversion',)
    list_display_links = (layer_link, featureversion_link, 'modification')
