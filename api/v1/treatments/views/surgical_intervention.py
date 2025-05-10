from rest_framework.viewsets import ModelViewSet

from api.v1.treatments.serializers.surgical_intervention import SurgicalInterventionSerializer
from apps.treatments.models import SurgicalIntervention


class SurgicalInterventionViewSet(ModelViewSet):
    queryset = SurgicalIntervention.objects.all()
    serializer_class = SurgicalInterventionSerializer
