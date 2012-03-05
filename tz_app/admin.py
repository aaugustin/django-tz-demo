from django.contrib import admin

from .models import Name, AutoName

class NameAdmin(admin.ModelAdmin):
    date_hierarchy = 'dated'
    list_display = ('name', 'dated')
    list_filter = ('dated',)
    ordering = ('dated',)

admin.site.register(Name, NameAdmin)

class AutoNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    ordering = ('created', 'updated')
    search_fields = ('name', 'created', 'updated')
    readonly_fields = ('created', 'updated')

admin.site.register(AutoName, AutoNameAdmin)
