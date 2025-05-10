from rest_framework.viewsets import ModelViewSet

from api.v1.treatments.serializers.patient import PatientSerializer
from apps.treatments.models import Patient


class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
