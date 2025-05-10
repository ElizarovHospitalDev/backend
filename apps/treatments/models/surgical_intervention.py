from django.db import models

from apps.treatments.models.operation_stage import OperationStage
from apps.treatments.models.treatment import Treatment


class SurgicalIntervention(models.Model):
    treatment = models.ForeignKey(
        Treatment,
        on_delete=models.CASCADE,
        verbose_name='Лечение',
    )
    operation_stage = models.ForeignKey(
        OperationStage,
        on_delete=models.CASCADE,
        verbose_name='Этап операции',
    )
    operation_date = models.DateField(
        verbose_name='Дата операции',
    )
    wound_character = models.CharField(
        max_length=255,
        verbose_name='Характер раны',
        blank=True,
    )
    drainage = models.CharField(
        max_length=255,
        verbose_name='Дренирование',
        blank=True,
    )
    complications = models.TextField(
        blank=True,
        null=True,
        verbose_name='Осложнения',
    )

    class Meta:
        verbose_name = 'Оперативное вмешательство'
        verbose_name_plural = 'Оперативные вмешательства'

    def __str__(self):
        return f"{self.operation_stage} — {self.operation_date}"
