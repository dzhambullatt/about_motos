from django.contrib import admin

from .models import *


class MotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published', 'photo', 'time_update')


class CatsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Moto, MotoAdmin)
admin.site.register(Cats, CatsAdmin)
