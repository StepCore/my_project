import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs/masks.log", "w")
file_formatter = logging.Formatter(
    "%(asctime)s %(levelname)s: %(filename)s %(funcName)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая возвращает маску карты."""
    card = []
    card_number = card_number.replace(" ", "")
    if card_number.isdigit() and len(card_number) == 16:
        card_number = card_number.replace(card_number[6:12], "******")
        for i in range(0, len(card_number), 4):
            card.append(card_number[i : i + 4])
        logger.debug("номер карты успешно скрыт")
        return " ".join(card)
    logger.error("некорректный формат данных")
    return "некорректный формат ввода данных"


def get_mask_account(account_number: str) -> str:
    """Функция, которая возвращает маску счета."""
    if len(account_number) >= 4 and account_number.isdigit():
        logger.debug("номер счета успешно скрыт")
        return "**" + account_number[-4:]
    logger.error("некорректный формат данных")
    return "некорректный формат ввода данных"
