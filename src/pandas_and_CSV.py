import csv

import pandas as pd


def csv_reader():
    """Функция, читающая CSV файл"""
    with open('../transactions.csv', mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        return list(reader)


# print(csv_reader())


def excel_reader():
    """Функция, читающая EXCEL файл"""
    reader = pd.read_excel("../transactions_excel.xlsx")
    return reader.to_dict(orient="records")


# print(excel_reader())
