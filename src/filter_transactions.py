import re

def filter_transaction(string):
    pattern = re.compile(string)
    matches = pattern.finditer(csv_reader())