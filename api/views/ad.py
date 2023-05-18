from rest_framework import generics, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.models import Ad
from api.serializers.ad import AdListSerializer


class AdViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):

    def get_queryset(self):
        return Ad.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return AdListSerializer
