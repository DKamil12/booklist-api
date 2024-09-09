from rest_framework import serializers
from books.models import Book, Author, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = []


class GenreInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = []


class AuthorInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']
    

class BookOnReadSerializer(serializers.ModelSerializer):
    genre = GenreInsertSerializer()
    author = AuthorInsertSerializer()
    
    class Meta:
        model = Book
        exclude = []


class BookOnWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = []


class BookInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title']
