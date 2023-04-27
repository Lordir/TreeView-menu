from django.contrib import admin
from .models import *


class TreeNodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'slug')
    list_display_links = ('id', 'name', 'parent', 'slug')


admin.site.register(TreeNodeModel, TreeNodeAdmin)
