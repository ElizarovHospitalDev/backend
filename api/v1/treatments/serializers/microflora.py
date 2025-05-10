from rest_framework import serializers

from apps.treatments.models import Microflora


class MicrofloraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Microflora
        fields = [
            'id',
            'microorganism',
            'mrse_mrsa',
            'pseudomonas_aeruginosa',
            'klebsiella_pneumoniae',
            'acinetobacter_baumanii',
            'treatment_fk',
        ]
