from django.db import models


class OperationStage(models.Model):
    name = models.CharField(
        verbose_name='Название этапа',
        max_length=255,
        unique=True,
    )

    class Meta:
        verbose_name = 'Этап операции'
        verbose_name_plural = 'Этапы операций'

    def __str__(self):
        return self.name
