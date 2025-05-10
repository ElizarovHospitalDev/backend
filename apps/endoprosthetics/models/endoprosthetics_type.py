from django.db import models


class EndoprostheticType(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )

    class Meta:
        verbose_name = 'Тип эндопротеза'
        verbose_name_plural = 'Типы эндопротезов'

    def __str__(self):
        return self.name
