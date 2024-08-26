import random

from src.file_readers import csv_reader, excel_reader
from src.filter_transactions import filter_transaction
from src.processing import sort_by_date
from src.utils import json_data
from src.widget import get_data, mask_account_card


def main():
    """Основная логика программы, связывание модулей и фильтрация транзакций"""
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\nВыберите необходимый пункт "
        "меню:(число от 1 до 3)\n1. Получить информацию о транзакциях из JSON-файла.\n2. Получить информацию о"
        "транзакциях из CSV-файла.\n3. Получить информацию о транзакциях из XLSX-файла"
    )
    file_list = [json_data(), csv_reader(), excel_reader()]
    filtered_transactions = []
    try:
        user_input = int(input())
        if user_input == 1:
            print("Для обработки выбран JSON-файл.")
            user_choice = json_data()
        elif user_input == 2:
            print("Для обработки выбран CSV-файл.")
            user_choice = csv_reader()
        elif user_input == 3:
            print("Для обработки выбран XLSX-файл.")
            user_choice = excel_reader()
        else:
            user_choice = random.randint(1, 3)
            print(f"Выбран случайный файл: {user_choice}")
            user_choice = file_list[user_choice - 1]
    except ValueError:
        user_choice = random.randint(1, 3)
        print(f"Выбран случайный файл: {user_choice}")
        user_choice = file_list[user_choice - 1]

    user_input = input(
        "Введите статус, по которому необходимо выполнить фильтрацию."
        "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
    )
    if user_input.lower() == "executed":
        print('Операции отфильтрованы по статусу "EXECUTED"')
        user_choice = filter_transaction(user_choice, "EXECUTED")
    elif user_input.lower() == "canceled":
        print('Операции отфильтрованы по статусу "CANCELED"')
        user_choice = filter_transaction(user_choice, "CANCELED")
    elif user_input.lower() == "pending":
        print('Операции отфильтрованы по статусу "PENDING"')
        user_choice = filter_transaction(user_choice, "PENDING")
    else:
        user_choice = filter_transaction(user_choice, "state")
        print(f'Статус операции "{user_input}" недоступен.')

    user_input = input("Отсортировать операции по дате? Да/Нет\n")
    if user_input.lower() == "да":
        user_choice = sort_by_date(user_choice)
        user_input = input("Отсортировать по возрастанию или по убыванию?\n")
        if user_input.lower() == "по возрастанию":
            user_choice = sort_by_date(user_choice, reverse=False)

    user_input = input("Выводить только рублевые тразакции? Да/Нет\n")
    if user_input.lower() == "да":
        user_choice = filter_transaction(user_choice, "RUB")

    user_input = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n"
    )
    if user_input.lower() == "да":
        user_input = input("Введите слово для фильтрации.\n")
        user_choice = filter_transaction(user_choice, user_input)

    for transaction in user_choice:
        if "operationAmount" in transaction:
            if transaction["description"] == "Открытие вклада":
                filtered_transactions.append(
                    f"{get_data(transaction.get('date'))} {transaction['description']}"
                    f"\n{mask_account_card(transaction.get('to'))}"
                    f"\nСумма: {transaction.get('operationAmount').get('amount')} "
                    f"{transaction.get('operationAmount').get('currency').get('code')}"
                )
            else:
                filtered_transactions.append(
                    f"{get_data(transaction.get('date'))} {transaction['description']}"
                    f"\n{mask_account_card(transaction.get('from'))} -> {mask_account_card(transaction.get('to'))}"
                    f"\nСумма: {transaction.get('operationAmount').get('amount')} "
                    f"{transaction.get('operationAmount').get('currency').get('code')}"
                )
        else:
            if transaction["description"] == "Открытие вклада":
                filtered_transactions.append(
                    f"{get_data(transaction.get('date'))} {transaction['description']}"
                    f"\n{mask_account_card(transaction.get('to'))}\nСумма: {transaction.get('amount')} "
                    f"{transaction.get('currency_code')}"
                )
            else:
                filtered_transactions.append(
                    f"{get_data(transaction.get('date'))} {transaction['description']}"
                    f"\n{mask_account_card(transaction.get('from'))} -> {mask_account_card(transaction.get('to'))}"
                    f"\nСумма: {transaction.get('amount')} {transaction.get('currency_code')}"
                )

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return []
    else:
        print(
            f"Распечатываю итоговый список транзакций...\nВсего банковских операций в выборке: {len(user_choice)}\n"
        )
        return filtered_transactions


# print(*main(), sep="\n\n")
