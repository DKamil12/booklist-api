from django.contrib import admin
from .models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'book', 'rating']
    list_display_links = ['id', 'user']
    list_filter = ['book', 'user', 'rating']


admin.site.register(Review, ReviewAdmin)