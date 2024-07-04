def get_mask_card_number(card_number: str) -> str:
    """Функция, которая возвращает маску карты."""
    card = []
    card_number = card_number.replace(" ", "")
    card_number = card_number.replace(card_number[6:12], "******")
    for i in range(0, len(card_number), 4):
        card.append(card_number[i : i + 4])
    return " ".join(card)


def get_mask_account(account_number: str) -> str:
    """Функция, которая возвращает маску счета."""
    return "**" + account_number[-4:]
