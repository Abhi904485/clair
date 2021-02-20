from django.contrib import admin

from .models import Lock


# Register your models here.


@admin.register(Lock)
class LockAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'until')
