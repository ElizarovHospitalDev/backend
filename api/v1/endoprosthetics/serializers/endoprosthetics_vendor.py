from rest_framework import serializers

from apps.endoprosthetics.models import EndoprostheticVendor


class EndoprostheticVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndoprostheticVendor
        fields = [
            'id',
            'name',
        ]
