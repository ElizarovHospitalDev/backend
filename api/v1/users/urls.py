from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.v1.users import views
from api.v1.users.views.password_recovery import PasswordResetView
from api.v1.users.views.password_recovery_confirm import PasswordResetConfirmView


router = SimpleRouter()

router.register('users', views.UserViewSet)


urlpatterns = [
    path(
        'password/reset/',
        PasswordResetView.as_view(),
        name='password_reset',
    ),
    path(
        'password/reset/confirm/',
        PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'tokens/',
        TokenObtainPairView.as_view(),
        name='user_tokens',
    ),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh',
    ),
] + router.urls
