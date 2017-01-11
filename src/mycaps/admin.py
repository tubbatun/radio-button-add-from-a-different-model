from django import forms
from django.contrib import admin
from django.utils.html import mark_safe

from . import models

@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
        pass

@admin.register(models.Coffee)
class CoffeeAdmin(admin.ModelAdmin):
        pass

# Admin
@admin.register(models.Package)
class PackageAdmin(admin.ModelAdmin):
    pass
    # list_display = [
    #     'title',
    #     'active',
    # ]
    # list_filter = [
    #     'active',
    # ]
