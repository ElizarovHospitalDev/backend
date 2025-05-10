from rest_framework.viewsets import ModelViewSet

from api.v1.endoprosthetics.serializers.endoprosthetics_vendor import EndoprostheticVendorSerializer
from apps.endoprosthetics.models import EndoprostheticVendor


class EndoprostheticVendorViewSet(ModelViewSet):
    queryset = EndoprostheticVendor.objects.all()
    serializer_class = EndoprostheticVendorSerializer
