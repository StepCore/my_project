from typing import Any


def mask_account_card(string: Any) -> str:
    """Функция, которая возвращает маску карты."""
    card = []
    string = string.split()
    for i in string:
        if i.isdigit():
            masked_num = i[:-10] + "******" + i[-4:]
        elif i == "Счет":
            return "Счет **" + string[1][-4:]
        else:
            card.append(i)
    for i in range(0, len(masked_num), 4):
        card.append(masked_num[i: i + 4])
    return " ".join(card)


print(mask_account_card("Visa Gold 5999414228426353"))


def get_data(string: str) -> str:
    '''Функция, которая возвращает корректную дату'''
    return string[8:10] + "." + string[5:7] + "." + string[:4]


print(get_data("2018-07-11T02:26:18.671407"))
