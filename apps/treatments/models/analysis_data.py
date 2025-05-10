from django.db import models


class AnalysisData(models.Model):
    KAK = models.CharField(
        'КАК',
        max_length=255,
        blank=True,
    )
    VKAK = models.CharField(
        'ВКАК',
        max_length=255,
        blank=True,
    )
    urine_test = models.CharField(
        'Анализ мочи',
        max_length=255,
        blank=True,
    )
    treatment = models.ForeignKey(
        'Treatment',
        on_delete=models.CASCADE,
    )
