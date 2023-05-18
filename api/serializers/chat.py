from api.models import User, Message
from api.models.chat import Chat
from api.serializers.user import UserSerializer
from rest_framework import serializers


class LastMessageSerializer(serializers.Serializer):
    text = serializers.CharField()
    sender = serializers.EmailField()
    created_at = serializers.DateTimeField()


class ChatListSerializer(serializers.ModelSerializer):
    last_message = LastMessageSerializer()

    class Meta:
        model = Chat
        fields = ["id", "last_message"]


class MessageCreateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=528, required=True)

    def pre_create(self, validated_data):
        sender = self.context["request"].user
        if not (sender in self.context["chat"].participants.all()):
            raise serializers.ValidationError("User isn't participant of the chat.")
        return Message.objects.create(
            sender=sender,
            text=validated_data["text"],
            chat=self.context["chat"]
        )
