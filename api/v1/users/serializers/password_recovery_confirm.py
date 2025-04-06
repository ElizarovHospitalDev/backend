from rest_framework import serializers


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password1 = serializers.CharField(
        label='Новый пароль',
        max_length=128,
    )
    new_password2 = serializers.CharField(
        label='Новый пароль',
        max_length=128,
    )
    uid = serializers.CharField(
        label='UID',
    )
    token = serializers.CharField(
        label='Token',
    )
