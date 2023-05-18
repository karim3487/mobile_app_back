from django.db import models

from api.models.base import BaseDatesModel


class Ad(BaseDatesModel):
    creator = models.ForeignKey(
        "User",
        on_delete=models.SET_NULL,
        related_name="ads",
        null=True,
        blank=False,
        help_text="User who created ad."
    )

    title = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        help_text="Title of ad."
    )

    text = models.TextField(
        null=True,
        blank=True,
        help_text="Text of ad."
    )

    class Meta:
        ordering = ["-created_at"]
