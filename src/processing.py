def filter_by_state(
    list_of_data: str,
    state="EXECUTED",
) -> list[str]:
    '''Функция, которая возвращает список словарей, отсортированный по категории "state"'''
    right_list = []
    for transaction in list_of_data:
        if transaction.get("state") == state:
            right_list.append(transaction)
    if not right_list:
        return "некоректный формат ввода данных"
    return right_list


def sort_by_date(list_of_data: str, reverse=True) -> list[str]:
    """Функция, которая возвращает список словарей, отсортированный по дате"""
    return sorted(list_of_data, key=lambda x: x["date"], reverse=reverse)
