from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .api.api_views import ReviewAPIViewSet

router = SimpleRouter()
router.register(r'reviews', ReviewAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
]