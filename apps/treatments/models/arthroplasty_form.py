from django.db import models


class ArthroplastyForm(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )

    class Meta:
        verbose_name = 'Вид артропластики'
        verbose_name_plural = 'Виды артропластики'

    def __str__(self):
        return self.name
