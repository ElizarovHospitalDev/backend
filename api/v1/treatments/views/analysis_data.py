from rest_framework.viewsets import ModelViewSet

from api.v1.treatments.serializers.analysis_data import AnalysisDataSerializer
from apps.treatments.models import AnalysisData


class AnalysisDataViewSet(ModelViewSet):
    queryset = AnalysisData.objects.all()
    serializer_class = AnalysisDataSerializer
