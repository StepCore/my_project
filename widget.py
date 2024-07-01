from typing import Any


def mask_account_card(card_number: str) -> str:
    """Функция, которая возвращает маску карты."""
    card = []
    card_number = card_number.split()
    for i in card_number:
        if i.isdigit():
            masked_num = i[:-10] + "******" + i[-4:]
        elif i == "Счет":
            return "Счет **" + card_number[1][-4:]
        else:
            card.append(i)
    for i in range(0, len(masked_num), 4):
        card.append(masked_num[i: i + 4])
    return " ".join(card)


print(mask_account_card("Visa Platinum 5999414228426353"))


def get_data(account_number: str) -> str:
    '''Функция, которая возвращает корректную дату'''
    return account_number[8:10] + "." + account_number[5:7] + "." + account_number[:4]


print(get_data("2018-07-11T02:26:18.671407"))
