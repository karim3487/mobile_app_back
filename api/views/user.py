from django.apps import apps
from django.db.models import Subquery, OuterRef
from django.db.models.functions import JSONObject
from rest_framework import generics, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.models import User
from api.permissions.permissions import UserAccessPolicy
from api.serializers.user import UserSerializer

from api.utils import filters as api_filters


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    permission_classes = (UserAccessPolicy,)

    def get_queryset(self):
        return UserAccessPolicy.scope_queryset(self.request, User.objects.all(), self.action)

    def get_serializer_class(self):
        return UserSerializer
