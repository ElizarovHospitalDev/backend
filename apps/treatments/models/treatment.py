from django.db import models

from apps.treatments.models.arthroplasty_form import ArthroplastyForm
from apps.treatments.models.patient import Patient


class Treatment(models.Model):
    reason = models.CharField(
        'Причина артропластики',
        max_length=255,
        blank=True,
    )
    form = models.ForeignKey(
        ArthroplastyForm,
        on_delete=models.CASCADE,
        verbose_name='Вид артропластики',
    )
    therapy = models.TextField(
        'Полученное лечение',
        blank=True,
    )
    form_pjl = models.CharField(
        'Вид PJL',
        max_length=255,
        blank=True,
    )
    local_status = models.CharField(
        'Локальный статус',
        max_length=255,
        blank=True,
    )
    thigh_defect = models.CharField(
        'Дефект бедра по AORI',
        max_length=255,
        blank=True,
    )
    shin_defect = models.CharField(
        'Дефект голени по AORI',
        max_length=255,
        blank=True,
    )
    therapy_option = models.CharField(
        'Вариант лечения',
        max_length=255,
        blank=True,
    )
    patient = models.ForeignKey(
        Patient,
        verbose_name='Пациент',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Лечение'
        verbose_name_plural = 'Лечения'

    def __str__(self):
        return f"Лечение пациента {self.patient}"
