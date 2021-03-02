from django.contrib import admin

from clair.export import ExportCsvMixin, ExportPdfMixin
from .models import SchemaMigrations


# Register your models here.


@admin.register(SchemaMigrations)
class SchemaMigrationsAdmin(admin.ModelAdmin, ExportCsvMixin, ExportPdfMixin):
    list_display = ('version',)
    search_fields = ('version',)
    ordering = ('version',)
    list_per_page = 20
    list_display_links = ('version',)
    list_filter = ('version',)
    actions = ["export_as_csv", "export_as_pdf"]
