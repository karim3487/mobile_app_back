import os
import time

from django.db import models

from api.models.base import BaseDatesModel


def custom_upload_to(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return 'attachments/%s__time_%s%s' % (filename_base, round(time.time() * 1000), filename_ext.lower(),)


class Attachment(BaseDatesModel):
    file = models.FileField(
        upload_to=custom_upload_to,
    )

    title = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        help_text="Title of ad."
    )

    class Meta:
        ordering = ["title"]
