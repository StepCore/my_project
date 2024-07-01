from project_2 import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
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


def get_data(account_number: str) -> str:
    """Функция, которая возвращает корректную дату"""
    return account_number[8:10] + "." + account_number[5:7] + "." + account_number[:4]
