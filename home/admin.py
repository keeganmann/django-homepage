from django.contrib import admin
from models import NavItem, homepageFeature, HeaderImage, SidebarItem

class NavItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'ordering')

admin.site.register(NavItem, NavItemAdmin)

class homepageFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'ordering')#, 'url', 'imgurl', 'description')

admin.site.register(homepageFeature, homepageFeatureAdmin)

class HeaderImageAdmin(admin.ModelAdmin):
    list_display = ('reference', 'precedence')

admin.site.register(HeaderImage, HeaderImageAdmin)

class SidebarItemAdmin(admin.ModelAdmin):
    list_display = ('title', )

admin.site.register(SidebarItem, SidebarItemAdmin)
