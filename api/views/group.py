from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from api.models import Group
from api.serializers.group import GroupSerializer


class GroupViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):

    def get_queryset(self):
        return Group.objects.all()

    def get_serializer_class(self):
        return GroupSerializer
