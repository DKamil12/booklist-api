from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import permissions
from .serializers import ListOnReadSerializer, ListOnWriteSerializer, ListItemOnReadSerializer, ListItemOnWriteSerializer, ListFollowerOnReadSerializer, ListFollowerOnWriteSerializer
from lists.models import List, ListItem, ListFollower
from users.permissions import IsOwnerOrReadOnly, HasListOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


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


class ListItemsAPIViewSet(ModelViewSet):
    queryset = ListItem.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, HasListOrReadOnly]
    search_fields = ['list__name', 'list__user__username', 'book__title', 'book__author__name']
    filterset_fields = ['book__genre']
    
    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return ListItemOnReadSerializer
        else:
            return ListItemOnWriteSerializer


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
        serializer.save(user=self.request.user)