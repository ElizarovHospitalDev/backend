from rest_framework.viewsets import ModelViewSet

from api.v1.endoprosthetics.serializers.endoprosthetics import EndoprostheticSerializer
from apps.endoprosthetics.models import Endoprosthetic


class EndoprostheticViewSet(ModelViewSet):
    queryset = Endoprosthetic.objects.all()
    serializer_class = EndoprostheticSerializer
