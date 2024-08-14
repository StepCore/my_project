from unittest.mock import patch

from src.external_api import convert_to_rub


@patch("src.external_api.requests.get")
def test_convert_to_rub(mock):
    mock.return_value.json.return_value = {"result": 31957.58}

    result = convert_to_rub(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {"name": "руб.", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    )

    assert result == 31957.58
