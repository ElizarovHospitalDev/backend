from dataclasses import dataclass
from functools import cached_property

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import get_default_password_validators
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from django.utils.http import urlsafe_base64_decode as uid_decoder

from utils.actions.abstract import AbstractAction
from utils.actions.exceptions import ActionValidateException


User = get_user_model()


@dataclass()
class UserPasswordResetUseCase(AbstractAction):
    new_password1: str
    new_password2: str
    uid: str
    token: str

    @property
    def user_uid(self) -> bytes:
        return uid_decoder(self.uid)

    @cached_property
    def user(self) -> User:
        return User._default_manager.filter(pk=self.user_uid).first()

    def validate(self):
        if self.new_password1 != self.new_password2:
            raise ActionValidateException('Пароли не совпадают')

        if not self.user:
            raise ActionValidateException('Неверный UID')

        if not default_token_generator.check_token(self.user, self.token):
            raise ActionValidateException('Ссылка недействительна, попробуйте еще раз')

        for validator in get_default_password_validators():
            try:
                validator.validate(self.new_password1, self.user)
            except ValidationError as error:
                raise ActionValidateException(error.messages[0])

    def action(self):
        self.user.set_password(self.new_password1)
        self.user.save()
