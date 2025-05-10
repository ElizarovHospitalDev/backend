from django.db import models


class ComorbidPathology(models.Model):
    obesity = models.BooleanField(
        'Ожирение',
        default=False,
    )
    diabetes_mellitus = models.BooleanField(
        'Сахарный диабет',
        default=False,
    )
    hepatitis = models.BooleanField(
        'Гепатит',
        default=False,
    )
    hiv = models.BooleanField(
        'ВИЧ',
        default=False,
    )
    hormonal_treatment = models.BooleanField(
        'Гормональное лечение',
        default=False,
    )
    treatment = models.ForeignKey(
        'Treatment',
        on_delete=models.CASCADE,
    )
