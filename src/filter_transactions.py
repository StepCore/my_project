import re
from src.pandas_and_CSV import csv_reader


def filter_transaction(string='id'):
    filtered_list = []
    pattern = re.compile(string, flags=re.IGNORECASE)
    list_transaction = csv_reader(read_file='../transactions.csv')
    for item in list_transaction:
        str_item = str(item)
        matches = pattern.findall(str_item)
        for match in matches:
            filtered_list.append(str_item)
    return filtered_list


print(*filter_transaction('19626'), sep='\n')
