from django.db import models

from apps.endoprosthetics.models.endoprosthetics_form import EndoprostheticForm
from apps.endoprosthetics.models.endoprosthetics_type import EndoprostheticType
from apps.endoprosthetics.models.endoprosthetics_vendor import EndoprostheticVendor
from apps.treatments.models.patient import Patient


class Endoprosthetic(models.Model):
    type = models.ForeignKey(
        EndoprostheticType,
        on_delete=models.PROTECT,
        verbose_name='Тип',
    )
    vendor = models.ForeignKey(
        EndoprostheticVendor,
        on_delete=models.PROTECT,
        verbose_name='Производитель',
    )
    batch = models.CharField(
        max_length=255,
        verbose_name='Партия',
    )
    date = models.DateField(
        verbose_name='Дата выпуска',
    )
    form = models.ForeignKey(
        EndoprostheticForm,
        on_delete=models.PROTECT,
        verbose_name='Вид',
    )
    stable = models.BooleanField(
        verbose_name='Стабильность эндопротеза',
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.PROTECT,
        verbose_name='Пациент',
    )

    class Meta:
        verbose_name = 'Эндопротез'
        verbose_name_plural = 'Эндопротезы'

    def __str__(self):
        return f"{self.type.name} - {self.vendor.name} ({self.date})"
