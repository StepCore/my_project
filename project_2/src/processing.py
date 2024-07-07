from typing import Any


def filter_by_state(
    list_of_data: Any,
    state="EXECUTED",
) -> Any:
    right_list = []
    for dict in list_of_data:
        if dict["state"] == state:
            right_list.append(dict)
    return right_list


def sort_by_date(list_of_data: Any, key="date", reverse=False) -> Any:
    return sorted(list_of_data, key=lambda x: x[key], reverse=reverse)
