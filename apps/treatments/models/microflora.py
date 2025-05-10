from django.db import models


class Microflora(models.Model):
    class MicroorganismChoices(models.TextChoices):
        MRSE_MRSA = 'mrse_mrsa', 'MRSE/MRSA'
        PSEUDOMONAS = 'pseudomonas_aeruginosa', 'Pseudomonas aeruginosa'
        KLEBSIELLA = 'klebsiella_pneumoniae', 'Klebsiella pneumoniae'
        ACINETOBACTER = 'acinetobacter_baumanii', 'Acinetobacter baumannii'

    microorganism = models.CharField(
        'Микроорганизм',
        max_length=50,
        choices=MicroorganismChoices.choices,
    )
    mrse_mrsa = models.BooleanField(
        default=False,
    )
    pseudomonas_aeruginosa = models.BooleanField(
        default=False,
    )
    klebsiella_pneumoniae = models.BooleanField(
        default=False,
    )
    acinetobacter_baumanii = models.BooleanField(
        default=False,
    )
    treatment_fk = models.ForeignKey(
        'Treatment',
        on_delete=models.CASCADE,
    )
