from rest_framework.viewsets import ModelViewSet

from api.v1.treatments.serializers.comobrid_pathologies import ComorbidPathologySerializer
from apps.treatments.models import ComorbidPathology


class ComorbidPathologyViewSet(ModelViewSet):
    queryset = ComorbidPathology.objects.all()
    serializer_class = ComorbidPathologySerializer
