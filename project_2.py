def get_mask_card_number(num: str) -> str:
    """Функция, которая возвращает маску карты."""
    card = []
    num = str(num).replace(str(num)[6:12], "******")
    for i in range(0, len(num), 4):
        card.append(num[i: i + 4])
    return " ".join(card)


def get_mask_account(account_number: str) -> str:
    """Функция, которая возвращает маску счета."""
    return "**" + account_number[-4:]
