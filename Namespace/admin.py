from django.contrib import admin
from django_admin_search.admin import AdvancedSearchAdmin

from clair.export import ExportCsvMixin, ExportPdfMixin
from .forms import NamespaceForm
from .models import Namespace


# Register your models here.

# class NamespaceModelInline(admin.TabularInline):
#     model = Feature
#     raw_id_fields = ("namespace",)
#     show_change_link = True
#     extra = 1
#       min_num = 2
#       max_num = 5



@admin.register(Namespace)
class NamespaceAdmin(AdvancedSearchAdmin, ExportCsvMixin, ExportPdfMixin):
    # inlines = (NamespaceModelInline,)
    list_display = ("id", 'name', 'version_format')
    search_fields = ("id", 'name', 'version_format',)
    ordering = ("id", 'name', 'version_format')
    list_per_page = 20
    list_filter = ('name', 'version_format')
    list_display_links = ("id", 'name', 'version_format',)
    actions = ["export_as_csv", "export_as_pdf"]
    search_form = NamespaceForm
