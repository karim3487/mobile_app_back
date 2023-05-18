from django.db.models import Subquery, OuterRef
from django.db.models.functions import JSONObject
from rest_framework import generics, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.viewsets import GenericViewSet

from api.models import Message
from api.models.chat import Chat, Participant
from api.permissions.permissions import ChatAccessPolicy
from api.serializers.chat import ChatListSerializer, MessageCreateSerializer

from api.utils import filters as api_filters


class ChatViewSet(GenericViewSet):

    permission_classes = (ChatAccessPolicy, )

    def get_queryset(self):
        return ChatAccessPolicy.scope_queryset(
            self.request,
            Chat.objects.all().prefetch_related("participants"),
            self.action
        )

    def get_serializer_class(self):
        if self.action == "mychats":
            return ChatListSerializer
        if self.action == "send_message":
            return MessageCreateSerializer

    @action(detail=False, methods=["GET"])
    def mychats(self, request, *args, **kwargs):

        qs = self.filter_queryset(self.get_queryset())

        ts = qs.values("id").annotate(
            last_message=Subquery(
                Message.objects.filter(chat=OuterRef("id")).values(
                    data=JSONObject(
                        text="text", sender="sender__email", created_at="created_at"
                    )
                )
            )
        )

        serializer = self.get_serializer(ts, many=True)

        return Response(serializer.data)

    @action(detail=True, methods=["POST"])
    def send_message(self, request, pk=None):
        context = {"request": request, "chat": self.get_object()}
        serializer = self.get_serializer(data=request.data,
                                         context=context)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
