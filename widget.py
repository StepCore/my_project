from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """Функция, которая возвращает маску карты."""
    card = ''
    name = ''
    for el in card_number:
        if el.isalpha() or el == ' ':
            name += el
        elif el.isdigit():
            card += el
    name = name.rstrip()
    if 'Счет' in card_number:
        return name + ' ' + get_mask_account(card)
    else:
        return name + ' ' + get_mask_card_number(card)

print(mask_account_card("Счет 4564 2313 21 48 9513"))

def get_data(account_number: str) -> str:
    """Функция, которая возвращает корректную дату"""
    if bool(account_number):
        return account_number[8:10] + '.' + account_number[5:7] + '.' + account_number[:4]
    return account_number
