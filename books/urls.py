from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .api.api_views import BookAPIViewSet, GenreAPIViewSet, AuthorAPIViewSet

router = SimpleRouter()
router.register(r'books', BookAPIViewSet)
router.register(r'genres', GenreAPIViewSet)
router.register(r'authors', AuthorAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
]