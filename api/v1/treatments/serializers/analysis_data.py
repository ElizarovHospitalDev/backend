from rest_framework import serializers

from apps.treatments.models import AnalysisData


class AnalysisDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisData
        fields = [
            'id',
            'KAK',
            'VKAK',
            'urine_test',
            'treatment',
        ]
