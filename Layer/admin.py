from django.contrib import admin
from django.db import models
from django.forms import TextInput

from .models import Layer


# Register your models here.


@admin.register(Layer)
class LayerAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': 147})},
    }
    list_display = ('name', 'namespace', 'parent')
    readonly_fields = ("namespace", "parent")
    search_fields = ('name', 'namespace__name', 'parent__name')
    ordering = ('name', 'namespace', 'parent')
    list_filter = ('namespace',)
    list_per_page = 20
    list_display_links = ('name', 'namespace', 'parent')
