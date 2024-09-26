from django.contrib import admin
from .models import ListItem, List, ListFollower

# Register your models here.
class ListAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'followers_count']
    list_display_links = ['id', 'name']
    list_filter = ['name', 'user']


class ListFollowerAdmin(admin.ModelAdmin):
    list_display = ['id', 'list', 'user']
    list_display_links = ['id', 'list']
    list_filter = ['list', 'user']


class ListItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'list', 'book']
    list_display_links = ['id', 'list']
    list_filter = ['list', 'book']


admin.site.register(List, ListAdmin)
admin.site.register(ListItem, ListItemAdmin)
admin.site.register(ListFollower, ListFollowerAdmin)