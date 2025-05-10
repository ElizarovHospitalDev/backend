from rest_framework.viewsets import ModelViewSet

from api.v1.treatments.serializers.microflora import MicrofloraSerializer
from apps.treatments.models import Microflora


class MicrofloraViewSet(ModelViewSet):
    queryset = Microflora.objects.all()
    serializer_class = MicrofloraSerializer
