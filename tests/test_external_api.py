from unittest.mock import patch
from unittest.mock import Mock

from src.utils import json_data
import pytest

from ..src.external_api import converter_value, return_sum_transaction


def test_return_sum_transaction(out_list_transaction):
    assert return_sum_transaction() == out_list_transaction


def test_converter_value_1():
    mock_converter = Mock(return_value="9824.07")
    converter_value = mock_converter
    assert converter_value == "9824.07"
    mock_converter.assert_called_once_with()


@patch("src.utils.get_exchange_rate")
def test_converter_value(mock_get_exchange_rate):
    mock_get_exchange_rate.return_value = (True, 568457.78)
    usd_transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }
    result = converter_value(usd_transaction)
    assert result == 568457.78
