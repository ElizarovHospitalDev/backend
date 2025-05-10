from rest_framework import serializers

from apps.treatments.models import ArthroplastyForm


class ArthroplastyFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArthroplastyForm
        fields = [
            'id',
            'name',
        ]
