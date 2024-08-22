import re
from collections import Counter
from src.pandas_and_CSV import csv_reader


def filter_transaction(string="id"):
    filtered_list = []
    pattern = re.compile(string, flags=re.IGNORECASE)
    list_transaction = csv_reader(read_file="../transactions.csv")
    for item in list_transaction:
        matches = pattern.findall(str(item))
        for match in matches:
            filtered_list.append(item)
    return filtered_list


# print(*filter_transaction(), sep='\n')


def filter_by_description(descriptions):
    filtered_transactions = [
        transaction
        for transaction in filter_transaction("id")
        if transaction["description"] in descriptions
    ]
    description_counts = Counter(
        transaction["description"] for transaction in filtered_transactions
    )

    return description_counts


print(
    filter_by_description(
        [
            "Перевод организации",
            "Перевод с карты на карту",
            "Открытие вклада",
            "Перевод со счета на счет",
        ]
    )
)
