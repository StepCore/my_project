import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

from src.masks import get_mask_account, get_mask_card_number
from widget import get_data, mask_account_card


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

@pytest.mark.parametrize('value, expected', [('Visa Classic 7895325844526588', 'Visa Classic 7895 32** **** 6588'), ('MasterCard 7892 4567 7841 5562', 'MasterCard 7892 45** **** 5562'), ('Счет 786432489 410984123', 'Счет **4123')])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected

@pytest.mark.parametrize('value, expected', [('2024-03-11T02:26:18.671407', '11.03.2024'), ('','')])
def test_get_data(value, expected):
    assert get_data(value) == expected