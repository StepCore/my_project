import pytest

from ..src.decorators import log
from ..src.generators import filter_by_currency, gen, transaction_descriptions
from ..src.masks import get_mask_account, get_mask_card_number
from ..src.processing import filter_by_state, sort_by_date
from ..src.widget import get_data, mask_account_card


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


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Classic 7895325844526588", "Visa Classic 7895 32** **** 6588"),
        ("MasterCard 7892 4567 7841 5562", "MasterCard 7892 45** **** 5562"),
        ("Счет 786432489 410984123", "Счет **4123"),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "value, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("", "")]
)
def test_get_data(value, expected):
    assert get_data(value) == expected


@pytest.mark.parametrize(
    "list_input, state, expected",
    [
        (
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ],
            "EXECUTED",
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
            ],
        ),
        (
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ],
            "CANCELED",
            [
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ],
        ),
        ([], "", "некоректный формат ввода данных"),
    ],
)
def test_filter_by_state(list_input, state, expected):
    assert filter_by_state(list_input, state) == expected


@pytest.mark.parametrize(
    "value, reverse, expected",
    [
        (
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ],
            reverse := False,
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
            ],
        ),
        (
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ],
            reverse := True,
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
            ],
        ),
    ],
)
def test_sort_by_date(value, reverse, expected):
    assert sort_by_date(value, reverse=reverse) == expected


def test_transaction_descriptions(transactions):
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


def test_filter_by_currency(transactions):
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }, {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }


def test_gen(start_num, end_num):
    generator = gen(1000000000000000, 1000000000000005)
    assert next(generator) == "1000 0000 0000 0000"
    assert next(generator) == "1000 0000 0000 0001"
    assert next(generator) == "1000 0000 0000 0002"
    assert next(generator) == "1000 0000 0000 0003"
    assert next(generator) == "1000 0000 0000 0004"
    assert next(generator) == "1000 0000 0000 0005"


def test_log(capsys):
    @log()
    def func():
        return "output"

    func()
    captured = capsys.readouterr()
    assert captured.out == "func ok\n"


def test_error_log(capsys):
    @log()
    def error_function(x, y):
        raise ValueError("Something went wrong!")

    with pytest.raises(ValueError):  # Ожидаем, что будет выброшено исключение
        error_function(1, 2)

    captured = capsys.readouterr()
    assert "Start error_function" in captured.out
    assert "End error_function" in captured.out
