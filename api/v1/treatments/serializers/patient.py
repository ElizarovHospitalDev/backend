from rest_framework import serializers

from apps.treatments.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'birthday',
            'mobile_phone',
            'sex',
            'address',
        ]
