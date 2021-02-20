from django.contrib import admin

from .models import SchemaMigrations


# Register your models here.


@admin.register(SchemaMigrations)
class SchemaMigrationsAdmin(admin.ModelAdmin):
    list_display = ('version',)
    search_fields = ('version',)
    ordering = ('version',)
    list_per_page = 20
    list_display_links = ('version',)
    list_filter = ('version',)
