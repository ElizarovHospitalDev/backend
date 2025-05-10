from django.db import models

from apps.treatments.models.treatment import Treatment


class TreatmentOutcome(models.Model):
    treatment = models.OneToOneField(
        Treatment,
        on_delete=models.CASCADE,
        verbose_name='Лечение',
    )
    result = models.TextField(
        max_length=255,
        verbose_name='Реузльтат лечения',
    )
    artodesis = models.TextField(
        verbose_name='В случаях артодеза',
    )
    re_audit = models.TextField(
        verbose_name='Повторная ревизия',
    )
    outcome = models.TextField()

    class Meta:
        verbose_name = 'Исход лечения'
        verbose_name_plural = 'Исходы лечения'

    def __str__(self):
        return f"Исход для лечения {self.treatment.id}"
