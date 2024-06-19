from django.contrib import admin
from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status", "author", "date_created")
    list_filter = ("meal_type", "status", "date_created")
    search_fields = ("meal", "description")


admin.site.register(MenuItem, MenuItemAdmin)
