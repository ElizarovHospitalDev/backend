from rest_framework import serializers

from apps.treatments.models import SurgicalIntervention


class SurgicalInterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurgicalIntervention
        fields = [
            'id',
            'treatment',
            'operation_stage',
            'operation_date',
            'wound_character',
            'drainage',
            'complications',
        ]
