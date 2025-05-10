from rest_framework import serializers

from apps.endoprosthetics.models import EndoprostheticForm


class EndoprostheticFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndoprostheticForm
        fields = [
            'id',
            'name',
        ]
