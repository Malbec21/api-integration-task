from datetime import datetime

from validators import (validate_interval_value_hours,
                        validate_interval_unit,
                        validate_news_type,
                        validate_items)

MONTHS = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
          "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
          "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}


def prepare_datetime_object_from_api_date(date: str):
    date_list = date.split()
    year, month, day = int(date_list[3]), int(MONTHS[date_list[2]]), int(date_list[1])
    hour, minute, seconds = date_list[4].split(":")
    return datetime(year, month, day, int(hour), int(minute), int(seconds))


def prepare_datetime_object_from_day_start():
    date = datetime.now()
    return datetime(date.year, date.month, date.day)


def check_interval_unit_and_value(interval_unit: str, interval_value: int):
    interval_unit = validate_interval_unit(interval_unit)
    if interval_unit == 'hour':
        interval_value = validate_interval_value_hours(interval_value)
    return interval_unit, interval_value


def check_news_type(news_type):
    news_type = validate_news_type(news_type)
    return news_type


def check_items(items):
    items = validate_items(items)
    return items
