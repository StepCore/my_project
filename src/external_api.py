import json
import os

import requests
from dotenv import load_dotenv

load_dotenv("../.env")

HEADERS = json.loads(os.getenv("HEADERS"))


def convert_to_rub(transaction: dict) -> float:
    """Функция конвертации валюты в рубли"""
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return float(amount)
    else:
        response = requests.get(
            f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}",
            headers=HEADERS,
        )
        data = dict(response.json())
        return float(data["result"])
