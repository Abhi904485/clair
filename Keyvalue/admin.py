from django.contrib import admin

from clair.export import ExportCsvMixin, ExportPdfMixin
from .models import Keyvalue


# Register your models here.


@admin.register(Keyvalue)
class KeyValueAdmin(admin.ModelAdmin, ExportCsvMixin, ExportPdfMixin):
    list_display = ("id", "key", "value")
    search_fields = ("id", "key", "value")
    ordering = ("key", "value", "id")
    list_per_page = 20
    list_filter = ("key", "value")
    list_display_links = ("id", "key", "value", )
    actions = ["export_as_csv", "export_as_pdf"]
