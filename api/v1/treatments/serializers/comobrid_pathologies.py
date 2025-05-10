from rest_framework import serializers

from apps.treatments.models import ComorbidPathology


class ComorbidPathologySerializer(serializers.ModelSerializer):
    class Meta:
        model = ComorbidPathology
        fields = [
            'id',
            'obesity',
            'diabetes_mellitus',
            'hepatitis',
            'hiv',
            'hormonal_treatment',
            'treatment',
        ]
