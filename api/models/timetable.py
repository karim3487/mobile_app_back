from django.db import models

from api.const.choices import WeekDays
from .base import BaseDatesModel

WEEKDAYS = ["Mn", "Tw", "Wd", "Th", "Fr", "Sa", "Sn"]

# 1 Weektimetable (weekdays - empty)
# 2 WeekDayTable
# 3 DaySubject
# 4 set fk of WeekDayTable
# 5 WeekTimetable add created weekdaytable fk


class WeekTimetable(BaseDatesModel):
    is_even = models.BooleanField(default=False)
    group = models.ForeignKey(
        "Group",
        on_delete=models.CASCADE,
        related_name="timetables",
        blank=False,
        null=False,
        help_text="Target Group."
    )

    def __str__(self):
        return f"Is even: {self.is_even}"
        # return "Is even: {} {}".format(self.is_even, self.weekdays.count())


class Subject(BaseDatesModel):
    title = models.CharField(
        max_length=128,
        blank=False,
        null=False
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class WeekDayTable(BaseDatesModel):
    timetable = models.ForeignKey(
        "WeekTimetable",
        on_delete=models.CASCADE,
        related_name="weekdays",
        blank=False,
        null=False,
        help_text="Timetable that contains these days."
    )
    weekday = models.IntegerField(
        choices=WeekDays.choices,
        blank=False,
        null=False,
        help_text="Mn - 0, Tu - 1 ... Su - 6."
    )
    subjects = models.ManyToManyField(
        "Subject",
        through="DaySubject"
    )

    def __str__(self):
        return WEEKDAYS[self.weekday]


class DaySubject(BaseDatesModel):
    weekday = models.ForeignKey(
        WeekDayTable,
        on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        "Subject",
        on_delete=models.CASCADE
    )
    classroom = models.CharField(max_length=16, null=True, blank=True)
    start = models.TimeField(
        blank=True,
        null=True
    )
    end = models.TimeField(
        blank=True,
        null=True
    )

    def __str__(self):
        return "{} {}".format(self.weekday, self.subject)