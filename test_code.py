from project_2 import *

def mask_card(card_number: str) -> str:
    """Функция, которая возвращает маску карты."""
    card = []
    card_number = card_number.split()
    for i in card_number:
        if i.isdigit():
            card.append(get_mask_card_number(i))
            break
        elif i == "Счет":
            card.append(get_mask_account(card_number[1]))
            break
        card.append(i)
    return ' '.join(card)

print(mask_card('MasterCard 7158300734726758'))