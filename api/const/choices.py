from django.db import models
from django.utils.translation import gettext_lazy as _

CORRECT_CHOICE = "C"
INCORRECT_CHOICE = "I"


class WeekDays(models.IntegerChoices):
    MONDAY = 0, _("Monday")
    TUESDAY = 1, _("Tuesday")
    WEDNESDAY = 2, _("Wednesday")
    THURSDAY = 3, _("Thursday")
    FRIDAY = 4, _("Friday")
    SATURDAY = 5, _("Saturday")
    SUNDAY = 6, _("Sunday")