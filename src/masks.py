def get_mask_card_number(card_number: str) -> str:
    """Функция, которая возвращает маску карты."""
    card = []
    card_number = card_number.replace(" ", "")
    if card_number.isdigit() and len(card_number) == 16:
        card_number = card_number.replace(card_number[6:12], "******")
        for i in range(0, len(card_number), 4):
            card.append(card_number[i : i + 4])
        return " ".join(card)
    return "некорректный формат ввода данных"


def get_mask_account(account_number: str) -> str:
    """Функция, которая возвращает маску счета."""
    if len(account_number) >= 4 and account_number.isdigit():
        return "**" + account_number[-4:]
    return "некорректный формат ввода данных"
