from rest_framework.viewsets import ModelViewSet

from api.v1.endoprosthetics.serializers.endoprosthetics_form import EndoprostheticFormSerializer
from apps.endoprosthetics.models import EndoprostheticForm


class EndoprostheticFormViewSet(ModelViewSet):
    queryset = EndoprostheticForm.objects.all()
    serializer_class = EndoprostheticFormSerializer
