from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import ReviewOnReadSerializer, ReviewOnWriteSerializer
from reviews.models import Review
from users.permissions import IsOwnerOrReadOnly
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Reviews'])
class ReviewAPIViewSet(ModelViewSet):
    queryset = Review.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    search_fields = ['user__username', 'book__title', 'review_text']
    ordering_fields = ['raiting', 'created_at']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return ReviewOnReadSerializer
        else:
            return ReviewOnWriteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
