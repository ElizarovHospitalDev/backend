from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.v1.users.serializers.password_recovery_confirm import PasswordResetConfirmSerializer
from apps.users.actions.password_reset import UserPasswordResetUseCase
from utils.actions.controllers.view import ViewActionController


class PasswordResetConfirmView(GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = [permissions.AllowAny]

    @method_decorator(sensitive_post_parameters())
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ViewActionController(
            UserPasswordResetUseCase(**serializer.validated_data),
        ).execute()

        return Response(
            {'detail': 'Установлен пароль.'},
            status=status.HTTP_200_OK,
        )
