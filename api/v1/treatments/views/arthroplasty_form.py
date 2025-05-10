from rest_framework.viewsets import ModelViewSet

from api.v1.treatments.serializers.arthroplasty_form import ArthroplastyFormSerializer
from apps.treatments.models import ArthroplastyForm


class ArthroplastyFormViewSet(ModelViewSet):
    queryset = ArthroplastyForm.objects.all()
    serializer_class = ArthroplastyFormSerializer
