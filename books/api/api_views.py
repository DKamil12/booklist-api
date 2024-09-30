from rest_framework.viewsets import ModelViewSet
from books.models import Book, Author, Genre
from .serializers import BookOnReadSerializer, BookOnWriteSerializer, GenreSerializer, AuthorSerializer
from rest_framework import permissions
from users.permissions import IsStaffOrReadOnly
from books.filters import GenreFilter
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Books'])
class BookAPIViewSet(ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [IsStaffOrReadOnly]
    filterset_class = GenreFilter
    search_fields = ['title', 'author__name']
    ordering_fields = ['avg_rating']

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return BookOnReadSerializer
        else:
            return BookOnWriteSerializer


@extend_schema(tags=['Genres'])
class GenreAPIViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ['name', 'description']
    ordering_fields = ['name']
    # ascending ordering by default
    ordering = ['name']


@extend_schema(tags=['Authors'])
class AuthorAPIViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsStaffOrReadOnly]
    ordering_fields = ['name']
    search_fields = ['name']
    # ascending ordering by default
    ordering = ['name']