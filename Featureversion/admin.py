from django.contrib import admin

from .models import Featureversion


# Register your models here.


@admin.register(Featureversion)
class FeatureversionAdmin(admin.ModelAdmin):
    list_display = ("feature", "version")
    readonly_fields = ("feature",)
    search_fields = ("feature__name", "version")
    ordering = ("feature", "version")
    list_per_page = 20
    list_filter = ('version',)
    list_display_links = ("feature", "version")
