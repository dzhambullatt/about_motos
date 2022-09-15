from django.contrib import admin

from .models import *


class MotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published', 'photo', 'time_update')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class CatsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(Moto, MotoAdmin)
admin.site.register(Cats, CatsAdmin)
