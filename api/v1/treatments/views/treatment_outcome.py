from rest_framework.viewsets import ModelViewSet

from api.v1.treatments.serializers.treatment_outcome import TreatmentOutcomeSerializer
from apps.treatments.models import TreatmentOutcome


class TreatmentOutcomeViewSet(ModelViewSet):
    queryset = TreatmentOutcome.objects.all()
    serializer_class = TreatmentOutcomeSerializer
