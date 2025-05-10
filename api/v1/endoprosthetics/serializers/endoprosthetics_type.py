from rest_framework import serializers

from apps.endoprosthetics.models import EndoprostheticType


class EndoprostheticTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndoprostheticType
        fields = [
            'id',
            'name',
        ]
