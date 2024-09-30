from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.urls import router as books_router
from lists.urls import router as list_router
from reviews.urls import router as review_router
from users.urls import router as profile_router
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView


default_router = DefaultRouter()
default_router.registry.extend(list_router.registry)
default_router.registry.extend(review_router.registry)
default_router.registry.extend(books_router.registry)
default_router.registry.extend(profile_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('api/v1/', include(default_router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)