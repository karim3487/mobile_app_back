from django.db import models

from ..models.base import BaseDatesModel


class Professor(BaseDatesModel):
    full_name = models.CharField(
        blank=False,
        null=False
    )

    def __str__(self):
        return "Professor: {}".format(self.full_name)