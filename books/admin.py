from django.contrib import admin
from .models import Book, Author, Genre

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'bio']
    list_display_links = ['id', 'name']
    list_filter = ['name']


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'genre', 'avg_rating']
    list_display_links = ['id', 'title']
    list_filter = ['title', 'genre', 'author', 'avg_rating']


class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'short_description']
    list_display_links = ['id', 'name']
    list_filter = ['name']
    search_fields = ['description']

    def short_description(self, obj):
        return (obj.description[:145] + '...' if len(obj.description) > 145 else obj.description)
    
    short_description.short_description = 'Description'


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)