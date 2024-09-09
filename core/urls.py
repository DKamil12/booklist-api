from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.urls import router as books_router
from lists.urls import router as list_router
from reviews.urls import router as review_router
from users.urls import router as profle_router


default_router = DefaultRouter()
default_router.registry.extend(books_router.registry)
default_router.registry.extend(list_router.registry)
default_router.registry.extend(review_router.registry)
default_router.registry.extend(profle_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('api/v1/', include(default_router.urls)),
    # path('api/v1/lists/', include('lists.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)