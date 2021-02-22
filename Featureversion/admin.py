from django.contrib import admin
from django.utils.html import format_html

from .models import Featureversion


# Register your models here.


def feature_link(self):
    return format_html(
        '<a href="/{app_name}/{db_table}/{db_table_primary_key}/change/">{db_table_field}</a>'.format(
            app_name=self.feature._meta.app_label, db_table=self.feature._meta.db_table,
            db_table_primary_key=self.feature.id, db_table_field=self.feature.name))


feature_link.short_description = "Feature"
feature_link.admin_order_field = "feature"


@admin.register(Featureversion)
class FeatureversionAdmin(admin.ModelAdmin):
    list_display = (feature_link, "version")
    readonly_fields = ("feature",)
    search_fields = ("feature__name", "version")
    ordering = ("version",)
    list_per_page = 20
    list_filter = ('version',)
    list_display_links = (feature_link, "version")
