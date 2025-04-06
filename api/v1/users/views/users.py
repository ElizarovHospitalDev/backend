from django.contrib.auth import get_user_model
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.v1.users.serializers.users import UserSerializer


User = get_user_model()


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    representation_query_fields = ('first_name', 'last_name', 'middle_name')
