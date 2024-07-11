def filter_by_state(
    list_of_data: str,
    state="EXECUTED",
) -> list[str]:
    '''Функция, которая возвращает список словарей, отсортированный по категории "state"'''
    right_list = []
    for dict in list_of_data:
        if dict["state"] == state:
            right_list.append(dict)
    return right_list


def sort_by_date(list_of_data: str, key="date", reverse=True) -> list[str]:
    """Функция, которая возвращает список словарей, отсортированный по дате"""
    return sorted(list_of_data, key=lambda x: x[key], reverse=reverse)
