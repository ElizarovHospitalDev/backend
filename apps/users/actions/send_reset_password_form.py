from dataclasses import dataclass
from functools import cached_property

from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm

from utils.actions.abstract import AbstractAction


@dataclass
class SendResetPasswordForm(AbstractAction):
    email: str
    is_user_create: bool
    is_secure: bool = settings.FRONTEND_HOST.startswith('https')

    @cached_property
    def reset_form(self):
        return PasswordResetForm(data={'email': self.email})

    def validate(self):
        self.reset_form.is_valid()

    def action(self):
        body_email: str = 'create_user_email.html' if self.is_user_create else 'password_reset_email.html'

        opts = {
            'use_https': self.is_secure,
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
            'domain_override': settings.PASSWORD_RECOVERY_DOMAIN,
            'extra_email_context': {'url': settings.PASSWORD_RECOVERY_URL},
            'email_template_name': body_email,
        }
        self.reset_form.save(**opts)
