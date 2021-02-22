from django.contrib import admin
from django.db import models
from django.forms import TextInput
from django.utils.html import format_html

from .models import Layer


# Register your models here.


@admin.register(Layer)
class LayerAdmin(admin.ModelAdmin):
    def namespace_link(self):
        return format_html(
            '<a href="/{app_name}/{db_table}/{db_table_primary_key}/change/">{db_table_field}</a>'.format(
                app_name=self.namespace._meta.app_label, db_table=self.namespace._meta.db_table,
                db_table_primary_key=self.namespace.id, db_table_field=self.namespace.name))

    namespace_link.short_description = "Namespace"
    namespace_link.admin_order_field = "namespace"

    def parent_link(self):
        if self.parent is None:
            app_name = self._meta.app_label
            db_table = self._meta.db_table
            db_table_primary_key = self.id
            db_table_field = "-"
        else:
            app_name = self.parent._meta.app_label
            db_table = self.parent._meta.db_table
            db_table_primary_key = self.parent.id
            db_table_field = self.parent.name
        return format_html(
            '<a href="/{app_name}/{db_table}/{db_table_primary_key}/change/">{db_table_field}</a>'.format(
                app_name=app_name, db_table=db_table,
                db_table_primary_key=db_table_primary_key, db_table_field=db_table_field))

    parent_link.short_description = "Parent"
    parent_link.admin_order_field = "parent"

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': 150})},
    }
    list_display = ('name', namespace_link, parent_link)
    readonly_fields = ("namespace", "parent")
    search_fields = ('name', 'namespace__name', 'parent__name')
    ordering = ('name',)
    list_filter = ('namespace',)
    list_per_page = 20
    list_display_links = ('name', namespace_link, parent_link)
