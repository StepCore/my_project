import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "value, expected",
    [
        ("7895123587453254", "7895 12** **** 3254"),
        ("", "некорректный формат ввода данных"),
        ("7856421lkjhhgfdx321", "некорректный формат ввода данных"),
    ],
)
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("789565432489756498456", "**8456"),
        ("", "некорректный формат ввода данных"),
        ("7895654324897dfgjkldfgj56", "некорректный формат ввода данных"),
    ],
)
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected
