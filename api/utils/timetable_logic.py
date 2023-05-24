import datetime
from rest_framework.exceptions import ValidationError


# converts date to DateTime object
def get_date(date):
    date_format = "%Y-%m-%d"

    if date:
        try:
            date = date[:10]
            return datetime.datetime.strptime(date, date_format)
        except:
            raise ValidationError(
                f"Invalid key format: {date}. "
                f"Properly format: {date_format}")
    return None


def is_even_week(date):
    start_date = datetime.date(2023, 2, 5)
    delta = date.date() - start_date
    week_number = delta.days // 7

    return week_number % 2 == 0


def get_week_timetable(qs, date):
    if is_even_week(date):
        return qs.filter(is_even=True)
    return qs.filter(is_even=False)


def get_day_timetable(qs, today):
    current_week, today = get_week_timetable(qs, today)
    return current_week.filter(day=today.dayofweek)


def get_monday_and_sunday_of_week(date):
    monday = date - datetime.timedelta(days=date.weekday())
    sunday = date + datetime.timedelta(days=6 - date.weekday())
    return monday, sunday
