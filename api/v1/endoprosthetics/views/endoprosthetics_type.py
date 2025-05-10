from rest_framework.viewsets import ModelViewSet

from api.v1.endoprosthetics.serializers.endoprosthetics_type import EndoprostheticTypeSerializer
from apps.endoprosthetics.models import EndoprostheticType


class EndoprostheticTypeViewSet(ModelViewSet):
    queryset = EndoprostheticType.objects.all()
    serializer_class = EndoprostheticTypeSerializer
