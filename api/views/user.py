from django.apps import apps
from django.db.models import Subquery, OuterRef
from django.db.models.functions import JSONObject
from rest_framework import generics, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.models import Participant, User, Chat
from api.permissions.permissions import UserAccessPolicy
from api.serializers.user import UserSerializer

from api.utils import filters as api_filters

class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    permission_classes = (UserAccessPolicy, )

    def get_queryset(self):
        return UserAccessPolicy.scope_queryset(self.request, User.objects.all(), self.action)

    def get_serializer_class(self):
        return UserSerializer

    @action(detail=True, methods=["GET"])
    def start_conversation(self, request, pk=None):
        user = self.get_object()

        if request.user.chats.filter(id__in=user.chats.all()):
            return Response(status=status.HTTP_200_OK)
        new_chat = apps.get_model("api", "Chat").objects.create()
        Participant.objects.create(
            chat=new_chat,
            user=request.user
        )
        Participant.objects.create(
            chat=new_chat,
            user=user
        )
        return Response(status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["GET"])
    def available_partners(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        partners = api_filters.available_partners(
            Chat.objects.filter(id__in=request.user.chats.all()), request.user
        ).values("user").distinct()
        serializer = self.get_serializer(qs.filter(id__in=partners), many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["GET"])
    def my_partners(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        qs = qs.filter(chats__in=request.user.chats.all())
        serializer = self.get_serializer(qs.distinct(), many=True)
        return Response(serializer.data)
