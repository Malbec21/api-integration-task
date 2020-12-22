# Task 1

Write a code to show only negative news that happened on the stock market in past 24 hours.
Ability to find news by ticker name.

--------

**How to run**:
* Clone project
* pip3 install -r requirements.txt
* python3 main.py in project directory

**Functional**:
* You can by specifying these config params get the data you need: items, ticker, news_type, interval_unit, interval_value.

#####To get negative news in past 24 hours
Example:
```
items = 50
ticker = 'TSLA'
news_type = 'negative'
interval_unit = 'hour'
interval_value = 24
```

#####To get positive news in past 3 days
Example:
```
items = 50
ticker = 'TSLA'
news_type = 'positive'
interval_unit = 'day'
interval_value = 3
```