import datetime
from datetime import timedelta
from pprint import pprint

import requests
from dateutil.relativedelta import relativedelta

from config import Config as c
from utils import (check_items,
                   check_news_type,
                   check_interval_unit_and_value,
                   prepare_datetime_object_from_api_date,
                   prepare_datetime_object_from_day_start)


class NewsController:
    def __init__(self, items: int, ticker: str, news_type: str, interval_value: int, interval_unit: str) -> None:
        self.api_token = c.api_token
        self.ticker = ticker
        self.items = check_items(items)
        self.news_type = check_news_type(news_type)
        self.interval_unit, self.interval_value = check_interval_unit_and_value(interval_unit, interval_value)

    def get_news_response(self) -> list:
        api_response = self.get_api_news_response()
        news_response = self.prepare_news_response(api_response)
        return news_response

    def get_api_news_response(self) -> dict:
        api_response = requests.get(c.api_url + f'tickers={c.ticker}&items={c.items}&token={c.api_token}').json()
        return api_response

    def prepare_news_response(self, api_response: dict) -> list:
        """prepare news response by init params"""
        prepared_news = []
        start_day_date = prepare_datetime_object_from_day_start()
        if self.interval_unit == 'hour':
            prepared_news = self.check_and_filter_news_data(api_response, prepared_news, start_day_date)
        elif self.interval_unit == 'day':
            start_date = start_day_date - timedelta(days=self.interval_value)
            prepared_news = self.check_and_filter_news_data(api_response, prepared_news, start_date)
        elif self.interval_unit == 'week':
            start_date = start_day_date - timedelta(weeks=self.interval_value)
            prepared_news = self.check_and_filter_news_data(api_response, prepared_news, start_date)
        elif self.interval_unit == 'month':
            start_date = start_day_date - relativedelta(months=self.interval_value)
            prepared_news = self.check_and_filter_news_data(api_response, prepared_news, start_date)
        elif self.interval_unit == 'year':
            start_date = start_day_date - relativedelta(year=self.interval_value)
            prepared_news = self.check_and_filter_news_data(api_response, prepared_news, start_date)
        return prepared_news

    def check_and_filter_news_data(self, api_response: dict, prepared_news: list, start_date: datetime) -> list:
        for news in api_response.get('data'):
            news_date = prepare_datetime_object_from_api_date(news.get('date'))
            if news_date > start_date and self.news_type.capitalize() == news.get('sentiment'):
                prepared_news.append(news)
        return prepared_news


if __name__ == '__main__':
    news_controller = NewsController(c.items, c.ticker, c.news_type, c.interval_value, c.interval_unit)
    response = news_controller.get_news_response()
    pprint(response)
