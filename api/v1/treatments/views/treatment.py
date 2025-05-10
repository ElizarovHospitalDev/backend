from rest_framework.viewsets import ModelViewSet

from api.v1.treatments.serializers.treatment import TreatmentSerializer
from apps.treatments.models import Treatment


class TreatmentViewSet(ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
