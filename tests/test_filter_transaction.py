from unittest.mock import patch

from src.file_readers import csv_reader, excel_reader
from src.filter_transactions import filter_by_description, filter_transaction
from src.utils import json_data


@patch("src.filter_transactions.filter_transaction")
def test_filter_transaction(mock):
    mock.return_value.json.return_value = {
        "id": 2826625.0,
        "state": "EXECUTED",
        "date": "2022-01-21T02:42:20Z",
        "amount": 28564.0,
        "currency_name": "Krona",
        "currency_code": "SEK",
        "from": "Visa 2434960923372230",
        "to": "Счет 62389310054726732233",
        "description": "Перевод организации",
    }
    result = filter_transaction(excel_reader(), "282662")

    assert result == [
        {
            "id": 2826625.0,
            "state": "EXECUTED",
            "date": "2022-01-21T02:42:20Z",
            "amount": 28564.0,
            "currency_name": "Krona",
            "currency_code": "SEK",
            "from": "Visa 2434960923372230",
            "to": "Счет 62389310054726732233",
            "description": "Перевод организации",
        }
    ]


@patch("src.filter_transactions.filter_transaction")
def test_filter_transaction_2(mock):
    mock.return_value.json.return_value = []
    result = filter_transaction(json_data(), "pending")

    assert result == []


@patch("src.filter_transactions.filter_transaction")
def test_filter_transaction_3(mock):
    mock.return_value.json.return_value = [
        {
            "id": "439075",
            "state": "EXECUTED",
            "date": "2020-07-27T01:54:01Z",
            "amount": "28260",
            "currency_name": "Zloty",
            "currency_code": "PLN",
            "from": "American Express 3972065433339638",
            "to": "Visa 6170999529692389",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "5170766",
            "state": "PENDING",
            "date": "2023-01-11T18:41:24Z",
            "amount": "15534",
            "currency_name": "Quetzal",
            "currency_code": "GTQ",
            "from": "Счет 91269211633331489581",
            "to": "Счет 83962090923263746792",
            "description": "Перевод со счета на счет",
        },
        {
            "id": "2267444",
            "state": "EXECUTED",
            "date": "2022-07-26T02:51:10Z",
            "amount": "30971",
            "currency_name": "Euro",
            "currency_code": "EUR",
            "from": "Visa 8795333379584907",
            "to": "Счет 76145988629288763144",
            "description": "Перевод организации",
        },
    ]
    result = filter_transaction(csv_reader(), "3333")

    assert result == [
        {
            "id": "439075",
            "state": "EXECUTED",
            "date": "2020-07-27T01:54:01Z",
            "amount": "28260",
            "currency_name": "Zloty",
            "currency_code": "PLN",
            "from": "American Express 3972065433339638",
            "to": "Visa 6170999529692389",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "5170766",
            "state": "PENDING",
            "date": "2023-01-11T18:41:24Z",
            "amount": "15534",
            "currency_name": "Quetzal",
            "currency_code": "GTQ",
            "from": "Счет 91269211633331489581",
            "to": "Счет 83962090923263746792",
            "description": "Перевод со счета на счет",
        },
        {
            "id": "2267444",
            "state": "EXECUTED",
            "date": "2022-07-26T02:51:10Z",
            "amount": "30971",
            "currency_name": "Euro",
            "currency_code": "EUR",
            "from": "Visa 8795333379584907",
            "to": "Счет 76145988629288763144",
            "description": "Перевод организации",
        },
    ]


@patch("src.filter_transactions.filter_by_description")
def test_filter_by_description(mock):
    mock.return_value.json.return_value = {
        "Перевод с карты на карту": 660,
        "Открытие вклада": 208,
        "Перевод организации": 130,
        "Перевод со счета на счет": 120,
    }
    result = filter_by_description(
        descriptions=[
            "Перевод организации",
            "Перевод с карты на карту",
            "Открытие вклада",
            "Перевод со счета на счет",
        ]
    )

    assert result == {
        "Перевод с карты на карту": 660,
        "Открытие вклада": 208,
        "Перевод организации": 130,
        "Перевод со счета на счет": 120,
    }
