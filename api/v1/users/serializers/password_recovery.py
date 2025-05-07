from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.users.actions.send_reset_password_form import SendResetPasswordForm


User = get_user_model()


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label='Email',
    )

    def save(self):
        email = self.validated_data.get('email')
        request = self.context.get('request')

        if hasattr(settings, 'PASSWORD_RECOVERY_IS_SECURE'):
            is_secure = settings.PASSWORD_RECOVERY_IS_SECURE
        else:
            is_secure = True if request.scheme == 'https' else False

        SendResetPasswordForm(
            email=email,
            is_user_create=False,
            is_secure=is_secure,
        ).execute()
