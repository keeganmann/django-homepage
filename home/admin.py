from django.contrib import admin
from models import NavItem

class NavItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'ordering')

admin.site.register(NavItem, NavItemAdmin)