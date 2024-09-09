from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .api.api_view import RegisterView, UserAPIView, UserPersonalInfoAPIView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'users', UserAPIView)

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/profile/<int:pk>/', UserPersonalInfoAPIView.as_view(), name='profile'),
]
