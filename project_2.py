def get_mask_card_number(num: str) -> str:
    """Функция, которая возвращает маску карты."""
    card = []
    num = str(num).replace(str(num)[6:12], "******")
    for i in range(0, len(num), 4):
        card.append(num[i: i + 4])
    return " ".join(card)


print(get_mask_card_number(7000792289606361))


def get_mask_account(num: str) -> str:
    """Функция, которая возвращает маску счета."""
    return f"**{str(num)[-4:]}"


print(get_mask_account(1256412318697421))
