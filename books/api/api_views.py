from rest_framework.viewsets import ModelViewSet
from books.models import Book, Author, Genre
from .serializers import BookOnReadSerializer, BookOnWriteSerializer, GenreSerializer, AuthorSerializer
from rest_framework import permissions
from users.permissions import IsStaffOrReadOnly

class BookAPIViewSet(ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [IsStaffOrReadOnly]
    filterset_fields = ['genre']
    search_fields = ['title', 'author__name']
    ordering_fields = ['avg_rating']

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return BookOnReadSerializer
        else:
            return BookOnWriteSerializer


class GenreAPIViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ['name', 'description']
    ordering_fields = ['name']
    # ascending ordering by default
    ordering = ['name']


class AuthorAPIViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsStaffOrReadOnly]
    ordering_fields = ['name']
    search_fields = ['name']
    # ascending ordering by default
    ordering = ['name']