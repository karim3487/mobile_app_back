from datetime import datetime

from django.contrib.postgres.expressions import ArraySubquery
from django.db.models import OuterRef, F
from django.db.models.functions import JSONObject
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import WeekDayTable, Professor
from api.models.group import GroupProfessor, Group
from api.serializers.timetable import TimetableListSerializer
from api.utils import timetable_logic


def get_subject_by_day_ArraySubquery(filters):
    teachers_subquery = ArraySubquery(
        GroupProfessor.objects.filter(
            subject=OuterRef("daysubject__subject"),
            group=OuterRef(OuterRef("group"))
        ).annotate(
            t_id=F("professor__id"),
            name=F("professor__full_name")
        ).values(
            data=JSONObject(
                t_id="t_id",
                name="name",
            )
        )
    )

    return ArraySubquery(
        WeekDayTable.objects.filter(**filters)
        .filter(daysubject__subject__isnull=False)
        .annotate(
            data=JSONObject(
                id=F("daysubject__id"),
                title=F("daysubject__subject__title"),
                classroom=F("daysubject__classroom"),
                professors=teachers_subquery,
                start=F("daysubject__start"),
                end=F("daysubject__end"))
        ).order_by("daysubject__start").values_list("data", flat=True)
    )


date_param = openapi.Parameter('date', openapi.IN_QUERY,
                              description="Day of week that you search.",
                              required=False,
                              type=openapi.TYPE_STRING)


class TimetableWeekView(APIView):

    @swagger_auto_schema(
        responses={200: TimetableListSerializer(many=True)},
        manual_parameters=[date_param]
    )
    def get(self, request, code):
        """
        List timetable for specific group for current week.
        If you want to show timetable by specific date - proved day of this
        week in date param.
        If user is authenticated - notes will be available, otherwise - no.
        """

        # Get group
        group = get_object_or_404(Group, code=code)
        timetables = group.timetables.values(
            "is_even",
        )

        # get date, if no date use current date
        date = self.request.query_params.get("date", None)
        if date:
            date = timetable_logic.get_date(date)
        else:
            date = datetime.now()
        timetables = timetable_logic.get_week_timetable(
            timetables, date)

        # filter notes
        timetables = timetables.annotate(
            code=F("group__code"),
            day=F("weekdays__weekday"),
            all_subjects=get_subject_by_day_ArraySubquery(
                {"id__in": OuterRef("weekdays")}
            )
        ).order_by("is_even", "day")

        serializer = TimetableListSerializer(timetables, many=True)
        return Response(serializer.data)
