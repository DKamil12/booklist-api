from django.contrib import admin
from .models import ListItem, List, ListFollower

# Register your models here.
admin.site.register(List)
admin.site.register(ListItem)
admin.site.register(ListFollower)