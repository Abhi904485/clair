from django.contrib import admin

from clair.export import ExportCsvMixin, ExportPdfMixin
from .models import Lock


# Register your models here.


@admin.register(Lock)
class LockAdmin(admin.ModelAdmin, ExportCsvMixin, ExportPdfMixin):
    list_display = ("id", 'name', 'owner', 'until')
    actions = ["export_as_csv", "export_as_pdf"]
