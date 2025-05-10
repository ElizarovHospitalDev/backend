from django.db import models


class EndoprostheticVendor(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )

    class Meta:
        verbose_name = 'Производитель эндопротеза'
        verbose_name_plural = 'Производители эндопротезов'

    def __str__(self):
        return self.name
