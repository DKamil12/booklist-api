from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .api.api_views import ListAPIViewSet, ListItemsAPIViewSet, ListFollowerAPIViewSet

router = SimpleRouter()
router.register(r'lists', ListAPIViewSet)
router.register(r'list-items', ListItemsAPIViewSet)
router.register(r'list-followers', ListFollowerAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
]