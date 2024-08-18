import csv

import pandas as pd


def csv_reader(read_file):
    with open(read_file, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)


# print(csv_reader('../transactions.csv'))


def excel_reader(read_file):
    reader = pd.read_excel(read_file)
    print(dict(reader))


# print(excel_reader('../transactions_excel.xlsx'))
