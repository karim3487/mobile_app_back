import os
import time

from django.db import models

from api.models.base import BaseDatesModel


def custom_upload_to_teacher_images(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return 'teachers/%s__time_%s%s' % (filename_base, round(time.time() * 1000), filename_ext.lower())


class Teacher(BaseDatesModel):
    full_name = models.CharField(
        max_length=528,
        null=False,
        blank=False,
        help_text="Full name of the teacher."
    )

    job_title = models.CharField(
        max_length=528,
        null=False,
        blank=False,
        help_text="Job title."
    )

    image = models.URLField()
