import json
import os

import requests
from dotenv import load_dotenv

from src.utils import json_data

load_dotenv("../.env")

HEADERS = json.loads(os.getenv("HEADERS"))

list_transaction = []


def return_sum_transaction():
    """Функция, которая возвращает список сумм транзакций с пометками"""
    for dict_data in json_data():
        if (
            dict_data.get("operationAmount", {}).get("currency", {}).get("code")
            == "RUB"
        ):
            list_transaction.append(dict_data["operationAmount"]["amount"])
        elif (
            dict_data.get("operationAmount", {}).get("currency", {}).get("code")
            == "USD"
        ):
            list_transaction.append(
                dict_data["operationAmount"]["amount"] + " " + "USD"
            )
    return list_transaction


def converter_value():
    """Апи которое возвращает заданную сумму в рублях"""
    for summ in list_transaction:
        if "USD" in summ:
            amount = summ[:-4]
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount}"
            payload = {}
            response = requests.request("GET", url, headers=HEADERS, data=payload)
            status_code = response.status_code
            result = json.loads(response.text)
            list_transaction[list_transaction.index(summ)] = result["result"]
        return list_transaction


return_sum_transaction()
print(converter_value())
