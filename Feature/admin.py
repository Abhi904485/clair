from django.contrib import admin

from .models import Feature


# Register your models here.


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin, ):
    list_display = ("name", "namespace")
    readonly_fields = ("namespace",)
    search_fields = ('name', 'namespace__name',)
    ordering = ('name', 'namespace__name')
    list_per_page = 20
    list_display_links = ('name', 'namespace',)
