from src.utils import json_data
from src.filter_transactions import filter_transaction, filter_by_description
from src.pandas_and_CSV import csv_reader, excel_reader


def main():
    """Основная логика программы, связывание модулей и фильтрация транзакций"""
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\nВыберите необходимый пункт"
        "меню:\n1. Получить информацию о транзакциях из JSON-файла.\n2. Получить информацию о"
        "транзакциях из CSV-файла.\n3. Получить информацию о транзакциях из XLSX-файла"
    )
    while True:
        try:
            user_choice = int(input())
            if user_choice == 1:
                print('Для обработки выбран JSON-файл.')
                json_list_transaction = json_data()
                user_choice = json_list_transaction
                return json_list_transaction
            elif user_choice == 2:
                print('Для обработки выбран CSV-файл.')
                csv_list_transaction = csv_reader()
                user_choice = csv_list_transaction
                return user_choice
            elif user_choice == 3:
                print('Для обработки выбран XLSX-файл.')
                excel_list_transaction = excel_reader()
                user_choice = excel_list_transaction
            else:
                print('Пожалуйста, введите число от 1 до 3')
                continue
        except ValueError:
            print('Пожалуйста, введите число от 1 до 3')
        else:
            break

    while True:
        user_input = input('Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n')
        if user_input.lower() == 'executed':
            print('Операции отфильтрованы по статусу "EXECUTED"')
            filtered_by_executed = filter_transaction('EXECUTED')
        elif user_input.lower() == 'canceled':
            print('Операции отфильтрованы по статусу "CANCELED"')
            filtered_by_canceled = filter_transaction('CANCELED')
        elif user_input.lower() == 'pending':
            print('Операции отфильтрованы по статусу "PENDING"')
            filtered_by_pending = filter_transaction('PENDING')
        else:
            print(f'Статус операции "{user_input}" недоступен.')
            continue

    while True:
        user_input = input('Отсортировать операции по дате? Да/Нет\n')
        if user_input.lower() == 'да':
            break
        elif user_input.lower() == 'нет':
            break
        else:
            print('Пожалуйста, введите "да" или "нет"')
            continue

    while True:
        user_input = input('Отсортировать по возрастанию или по убыванию?\n')
        if user_input.lower() == 'по возрастанию':
            break
        elif user_input.lower() == 'по убыванию':
            break
        else:
            print('Пожалуйста, введите "по возрастанию" или "по убыванию"')
            continue

    while True:
        user_input = input('Выводить только рублевые тразакции? Да/Нет\n')
        if user_input.lower() == 'да':
            break
        elif user_input.lower() == 'нет':
            break
        else:
            print('Пожалуйста, введите "да" или "нет"')
            continue

    while True:
        user_input = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n')
        if user_input.lower() == 'да':
            break
        elif user_input.lower() == 'нет':
            break
        else:
            print('Пожалуйста, введите "да" или "нет"')
            continue


print(main())
