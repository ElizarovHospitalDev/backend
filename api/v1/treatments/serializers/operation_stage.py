from rest_framework import serializers

from apps.treatments.models import OperationStage


class OperationStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationStage
        fields = [
            'id',
            'name',
        ]
