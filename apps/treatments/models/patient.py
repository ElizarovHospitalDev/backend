from django.db import models


class PatientSexChoices(models.TextChoices):
    MAN = 'M', 'Мужской'
    WOMAN = 'W', 'Женский'


class Patient(models.Model):
    first_name = models.CharField(
        'Имя',
        max_length=255,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=255,
    )
    middle_name = models.CharField(
        'Отчество',
        max_length=255,
        blank=True,
        null=True,
    )
    birthday = models.DateField(
        'Дата рождения',
    )
    mobile_phone = models.CharField(
        'Номер телефона',
        max_length=20,
    )
    sex = models.CharField(
        'Пол',
        choices=PatientSexChoices.choices,
        max_length=1,
    )
    address = models.CharField(
        'Адрес',
        max_length=255,
    )

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
