import csv

import pandas as pd


def csv_reader(read_file):
    """Функция, читающая CSV файл"""
    with open(read_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        return list(reader)


# print(csv_reader('../transactions.csv'))


def excel_reader(read_file):
    """Функция, читающая EXCEL файл"""
    reader = pd.read_excel(read_file)
    return reader.to_dict(orient="records")


# print(excel_reader('../transactions_excel.xlsx'))
