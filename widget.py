from project_2 import *


def mask_card(card_number: str) -> str:
    """Функция, которая возвращает маску карты."""
    card = []
    name = []
    card_number = card_number.split()
    for i in card_number:
        if i == "Счет":
            name.append(i)
            card.append(card_number[1])
            return " ".join(name) + " " + get_mask_account(" ".join(card))
        elif i.isalpha():
            name.append(i)
        else:
            card.append(i)
    return " ".join(name) + " " + get_mask_card_number(" ".join(card))


print(mask_card("Visa Gold 5999414228426353"))


def get_data(account_number: str) -> str:
    """Функция, которая возвращает корректную дату"""
    return account_number[8:10] + "." + account_number[5:7] + "." + account_number[:4]


print(get_data("2018-07-11T02:26:18.671407"))
