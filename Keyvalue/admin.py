from django.contrib import admin

from .models import Keyvalue


# Register your models here.


@admin.register(Keyvalue)
class KeyValueAdmin(admin.ModelAdmin):
    list_display = ("key", "value")
    search_fields = ("key", "value")
    ordering = ("key", "value")
    list_per_page = 20
    list_filter = ("key", "value")
    list_display_links = ("key", "value")
