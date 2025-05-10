from rest_framework import serializers

from apps.treatments.models import Treatment


class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = [
            'id',
            'reason',
            'form',
            'therapy',
            'form_pjl',
            'local_status',
            'thigh_defect',
            'shin_defect',
            'therapy_option',
            'patient',
        ]
