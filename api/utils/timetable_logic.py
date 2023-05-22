from datetime import datetime, timedelta
from rest_framework.exceptions import ValidationError


# converts date to DateTime object
def get_date(date):
    date_format = "%Y-%m-%d"

    if date:
        try:
            date = date[:10]
            return datetime.strptime(date, date_format)
        except:
            raise ValidationError(
                f"Invalid key format: {date}. "
                f"Properly format: {date_format}")
    return None


def get_week_timetable(qs, date):
    return qs.filter(is_even=True)


def get_day_timetable(qs, today):
    current_week, today = get_week_timetable(qs, today)
    return current_week.filter(day=today.dayofweek)


def get_monday_and_sunday_of_week(date):
    monday = date - timedelta(days=date.weekday())
    sunday = date + timedelta(days=6-date.weekday())
    return monday, sunday