from rest_framework.viewsets import ModelViewSet

from api.v1.treatments.serializers.operation_stage import OperationStageSerializer
from apps.treatments.models import OperationStage


class OperationStageViewSet(ModelViewSet):
    queryset = OperationStage.objects.all()
    serializer_class = OperationStageSerializer
