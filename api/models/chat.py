from django.db import models

from api.models.base import BaseDatesModel


class Chat(BaseDatesModel):

    def __str__(self):
        return str(self.id)


class Participant(BaseDatesModel):
    chat = models.ForeignKey(
        "Chat",
        null=False,
        on_delete=models.CASCADE,
        related_name="participants",
        blank=False,
        help_text="Chat."
    )
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        blank=False,
        related_name="chats",
        null=False,
        help_text="Participant of the chat."
    )

    class Meta:
        unique_together = ("chat", "user", )
