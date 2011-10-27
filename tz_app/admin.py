from django.contrib import admin

from .models import Name, AutoName

class NameAdmin(admin.ModelAdmin):
    list_display = ('name', 'dated')
    date_hierarchy = 'dated'

admin.site.register(Name, NameAdmin)

class AutoNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    list_filter = ('created', 'updated')
    readonly_fields = ('created', 'updated')

admin.site.register(AutoName, AutoNameAdmin)
