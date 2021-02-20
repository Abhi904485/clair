from django.contrib import admin

from .models import Namespace


# Register your models here.

# class NamespaceModelInline(admin.TabularInline):
#     model = Feature
#     readonly_fields = ("namespace",)
#     show_change_link = True
#     extra = 1
#       min_num = 2
#       max_num = 5



@admin.register(Namespace)
class NamespaceAdmin(admin.ModelAdmin):
    # inlines = (NamespaceModelInline,)
    list_display = ('name', 'version_format')
    search_fields = ('name', 'version_format',)
    ordering = ('name', 'version_format')
    list_per_page = 20
    list_filter = ('name', 'version_format')
    list_display_links = ('name', 'version_format',)
