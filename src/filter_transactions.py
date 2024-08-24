import re
from collections import Counter
from src.pandas_and_CSV import csv_reader, excel_reader
from src.utils import json_data


def filter_transaction(string="id"):
    """Функция, которая возвращает отфильтрованный по найденной строке список транзакций"""
    filtered_list = []
    pattern = re.compile(string, flags=re.IGNORECASE)
    list_transaction = json_data()
    for item in list_transaction:
        matches = pattern.findall(str(item))
        for match in matches:
            filtered_list.append(item)
    return filtered_list


# print(*filter_transaction('pending'), sep='\n')


def filter_json(string):
    transactions = []
    for transaction in json_data():
        if transaction.get('state') == string.upper():
            transactions.append(transaction)
    return transactions


# print(*filter_json('canceled'), sep='\n')


def filter_by_description(descriptions):
    """Функция, которая возвращает словарь, состоящий из названия и количества транзакций"""
    filtered_transactions = [
        transaction
        for transaction in filter_transaction("id")
        if transaction["description"] in descriptions
    ]
    description_counts = Counter(
        transaction["description"] for transaction in filtered_transactions
    )

    return description_counts


# print(filter_by_description(["Перевод организации","Перевод с карты на карту","Открытие вклада","Перевод со счета на счет"]))
