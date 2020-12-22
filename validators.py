from config import Config as c
from exceptions import StockHuntException


def validate_items(items):
    if items > 50:
        raise StockHuntException('INVALID_ITEMS')
    return items


def validate_news_type(news_type):
    if news_type not in c.news_types:
        raise StockHuntException('INVALID_NEWS_TYPE')
    return news_type


def validate_interval_unit(unit):
    if unit not in c.unit_values:
        raise StockHuntException('INVALID_UNIT')
    return unit


def validate_interval_value_hours(value):
    if value != 24:
        raise StockHuntException('INVALID_INTERVAL_VALUE')
