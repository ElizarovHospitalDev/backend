from rest_framework import serializers

from apps.treatments.models import TreatmentOutcome


class TreatmentOutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentOutcome
        fields = [
            'id',
            'treatment',
            'result',
            'artodesis',
            're_audit',
            'outcome',
        ]
