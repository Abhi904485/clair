from django.contrib import admin

from .models import LayerDiffFeatureversion


# Register your models here.


@admin.register(LayerDiffFeatureversion)
class LayerDiffFeatureversionAdmin(admin.ModelAdmin):
    list_display = ('layer', 'featureversion', 'modification')
    readonly_fields = ('layer', 'featureversion')
    search_fields = ('layer__name', 'featureversion__version', 'modification')
    ordering = ('layer', 'featureversion', 'modification')
    list_per_page = 20
    list_filter = ('modification', 'layer__namespace', 'featureversion',)
    list_display_links = ('layer', 'featureversion', 'modification')
