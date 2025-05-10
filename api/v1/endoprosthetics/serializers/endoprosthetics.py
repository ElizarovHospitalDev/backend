from rest_framework import serializers

from apps.endoprosthetics.models import Endoprosthetic


class EndoprostheticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endoprosthetic
        fields = [
            'id',
            'type',
            'vendor',
            'batch',
            'date',
            'form',
            'stable',
            'patient',
        ]
