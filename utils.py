import json

import requests
from decouple import config


API_KEY = config('API_KEY')
API_ENDPOINT = 'https://api.currencyapi.com/v3/latest'


def get_currencies() -> list:
    currency_codes = []
    with open('currency.json') as f:
        currency_data = json.load(f)
        for currency in currency_data:
            code, _ = list(currency.items())[0]
            currency_codes.append(code)
    return sorted(currency_codes)


def convert_currency(from_currency: str, to_currency: str, amount: float) -> float:
    query_params = {
        'apikey': API_KEY,
        'base_currency': from_currency,
        'currencies': to_currency
    }
    response = requests.get(API_ENDPOINT, params=query_params)
    currency_data = response.json()
    exchange_rate = currency_data['data'][to_currency]['value']
    exchanged_value = exchange_rate * amount
    return exchanged_value
