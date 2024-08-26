import re
from collections import Counter

from src.file_readers import csv_reader, excel_reader
from src.utils import json_data


def filter_transaction(open_file, string="state"):
    """Функция, которая принимает файл и возвращает отфильтрованный по найденной строке список транзакций"""
    transactions = []
    if open_file == csv_reader() or excel_reader():
        pattern = re.compile(string, flags=re.IGNORECASE)
        list_transaction = open_file
        for item in list_transaction:
            matches = pattern.findall(str(item))
            for match in matches:
                if not isinstance(item["state"], float):
                    transactions.append(item)
        return transactions
    else:
        for transaction in json_data():
            if transaction.get(string) == string:
                transactions.append(transaction)
        return transactions


# print(*filter_transaction(csv_reader(), '3333'), sep='\n')


def filter_by_description(descriptions):
    """Функция, которая возвращает словарь, состоящий из названия и количества транзакций"""
    filtered_transactions = [
        transaction
        for transaction in filter_transaction(excel_reader(), "id")
        if transaction["description"] in descriptions
    ]
    description_counts = Counter(
        transaction["description"] for transaction in filtered_transactions
    )

    return description_counts


# print(
#     filter_by_description(
#         [
#             "Перевод организации",
#             "Перевод с карты на карту",
#             "Открытие вклада",
#             "Перевод со счета на счет",
#         ]
#     )
# )
