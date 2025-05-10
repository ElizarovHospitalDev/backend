from django.db import models


class EndoprostheticForm(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Форма эндопротеза'
        verbose_name_plural = 'Формы эндопротезов'

    def __str__(self):
        return self.name
