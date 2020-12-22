class Config:
    # main app config
    api_token = 'xusz8djb6ajbvuthhk5kdoyfxhrfanbrc7aslinw'
    api_url = 'https://stocknewsapi.com/api/v1?'
    news_types = ('positive', 'negative', 'neutral')
    unit_values = ('hour', 'day', 'week', 'month', 'year')
    # controller config
    items = 50
    ticker = 'TSLA'
    news_type = 'negative'
    interval_unit = 'hour'
    interval_value = 24
