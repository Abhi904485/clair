from django.contrib import admin
from django.utils.html import format_html

from .models import Feature


# Register your models here.


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin, ):

    def namespace_link(self):
        return format_html(
            '<a href="/{app_name}/{db_table}/{db_table_primary_key}/change/">{db_table_field}</a>'.format(
                app_name=self.namespace._meta.app_label, db_table=self.namespace._meta.db_table,
                db_table_primary_key=self.namespace.id, db_table_field=self.namespace.name))

    namespace_link.short_description = "Namespace"
    namespace_link.admin_order_field = "namespace"

    def version_format_link(self):
        return format_html(
            '<a href="/{app_name}/{db_table}/{db_table_primary_key}/change/">{db_table_field}</a>'.format(
                app_name=self.namespace._meta.app_label, db_table=self.namespace._meta.db_table,
                db_table_primary_key=self.namespace.id, db_table_field=self.namespace.version_format))

    version_format_link.short_description = "Version Format"
    version_format_link.admin_order_field = "namespace__version_format"

    list_display = ("name", namespace_link, version_format_link)
    # readonly_fields = ("namespace",)
    search_fields = ('name', 'namespace__name', 'namespace__version_format')
    ordering = ('name',)
    list_per_page = 20
    list_filter = ('namespace__version_format', 'namespace__name',)
    list_display_links = ("name", namespace_link, version_format_link)
