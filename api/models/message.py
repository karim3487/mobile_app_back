from django.db import models

from api.models.base import BaseDatesModel


class Message(BaseDatesModel):
    sender = models.ForeignKey(
        "User",
        on_delete=models.SET_NULL,
        related_name="messages",
        null=True,
        blank=False,
        help_text="Who send message."
    )
    chat = models.ForeignKey(
        "Chat",
        on_delete=models.SET_NULL,
        related_name="messages",
        null=True,
        blank=False,
        help_text="Who receive message."
    )
    text = models.CharField(
        max_length=528,
        null=False,
        blank=False,
        help_text="Text of the message."
    )

    class Meta:
        ordering = ["-created_at"]
