from typing import Iterable

def filter_by_state(list_of_data: Iterable[list], state='EXECUTED', ) -> Iterable[list]:
    right_list = []
    for dict in list_of_data:
        if dict['state'] == state:
            right_list.append(dict)
    return right_list

print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], 'CANCELED'))


def sort_by_date(list_of_data: Iterable[list], key='date', reverse=False) -> Iterable[list]:
    return sorted(list_of_data, key=lambda x: x[key], reverse=reverse)

print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], reverse=True))