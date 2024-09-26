from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import ListOnReadSerializer, ListOnWriteSerializer, ListItemOnReadSerializer, ListItemOnWriteSerializer, ListFollowerOnReadSerializer, ListFollowerOnWriteSerializer
from lists.models import List, ListItem, ListFollower
from users.permissions import IsOwnerOrReadOnly, HasListOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from books.filters import GenreFilterForListItem
from rest_framework.exceptions import ValidationError
from django.db import IntegrityError 


class ListAPIViewSet(ModelViewSet):
    queryset = List.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    ordering_fields = ['created_at', 'followers_count']
    ordering = ['-created_at']
    search_fields = ['name', 'description', 'user__username']

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return ListOnReadSerializer
        else:
            return ListOnWriteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListItemsAPIViewSet(ModelViewSet):
    queryset = ListItem.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, HasListOrReadOnly]
    search_fields = ['list__name', 'list__user__username', 'book__title', 'book__author__name']
    filterset_class = GenreFilterForListItem
    
    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return ListItemOnReadSerializer
        else:
            return ListItemOnWriteSerializer
        
    def create(self, request, *args, **kwargs):
        list_id = request.data.get('list')
        book_id = request.data.get('book')

        if ListItem.objects.filter(list=list_id, book=book_id).exists():
            raise ValidationError('This item is already exists!')

        return super().create(request, *args, **kwargs)


class ListFollowerAPIViewSet(ModelViewSet):
    queryset = ListFollower.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    search_fields = ['list__name', 'user__username']

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return ListFollowerOnReadSerializer
        else:
            return ListFollowerOnWriteSerializer
    
    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except IntegrityError:
            raise ValidationError('You are already following the list')
