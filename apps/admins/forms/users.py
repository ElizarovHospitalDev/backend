import random
import string

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.http.request import HttpRequest

from apps.users.actions.send_reset_password_form import SendResetPasswordForm


User = get_user_model()


class CustomUserCreationForm(forms.ModelForm):
    """Форма для создания пользователя (только email и username)."""

    email = forms.EmailField(required=True, label='Почта')
    username = forms.CharField(required=True, label='Логин')

    class Meta:
        model = User
        fields = ('email', 'username')

    def save(self, commit=True):
        user = super().save(commit=False)
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        user.email = email
        user.username = username

        # генерация случайного пароля
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        user.set_password(password)
        if commit:
            user.save()
            SendResetPasswordForm(
                email.strip(),
                is_user_create=True,
            ).execute()
        return user


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'username'),
            },
        ),
    )

    def save_model(self, request: HttpRequest, obj, form, change):
        if not change:
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
            obj.set_password(password)
            SendResetPasswordForm(
                form.cleaned_data['email'],
                is_user_create=not bool(obj.id),  # если айди нет, значит это создание
            ).execute()
            super().save_model(request, obj, form, change)
        else:
            super().save_model(request, obj, form, change)
