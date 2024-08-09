from unittest.mock import Mock, patch

from ..src.external_api import convert_to_rub


def test_convert_to_rub():
    mock_converter = Mock(return_value="9824.07")
    convert_to_rub = mock_converter
    assert convert_to_rub == "9824.07"
    mock_converter.assert_called_once_with()


@patch("src.utils.get_exchange_rate")
def test_converter_value(mock_get_exchange_rate):
    mock_get_exchange_rate.return_value = (True, 5684.78)
    usd_transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "5684.78",
            "currency": {"name": "руб", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    result = convert_to_rub(usd_transaction)
    assert result == 5684.78
