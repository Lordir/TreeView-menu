from django.contrib import admin
from .models import *


class TreeNodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'slug', 'level', 'number_menu')
    list_display_links = ('id', 'name',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ["name"]
    fields = ['name', 'parent', 'slug', 'number_menu']


class NameParentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(TreeNodeModel, TreeNodeAdmin)
admin.site.register(NameParent, NameParentAdmin)
