from django.db import models

from api.models.base import BaseDatesModel


class Group(BaseDatesModel):
    code = models.CharField(
        max_length=64,
        blank=False,
        null=False
    )
    professors = models.ManyToManyField(
        "Professor",
        through="GroupProfessor"
    )

    def __str__(self):
        return self.code


class GroupProfessor(models.Model):
    professor = models.ForeignKey(
        "Professor",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Teacher of the group."
    )
    group = models.ForeignKey(
        "Group",
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        help_text="Group."
    )
    subject = models.ForeignKey(
        "Subject",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Discipline."
    )
