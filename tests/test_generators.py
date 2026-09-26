import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions() -> list[dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD",
                },
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "RUB",
                    "code": "RUB",
                },
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


# Тест функции фильтра списка операций по валюте
@pytest.mark.parametrize(
    "currency, expected",
    [
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {
                        "amount": "9824.07",
                        "currency": {
                            "name": "USD",
                            "code": "USD",
                        },
                    },
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
        ),
        (
            "RUB",
            [
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {
                        "amount": "79114.93",
                        "currency": {
                            "name": "RUB",
                            "code": "RUB",
                        },
                    },
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                }
            ],
        ),
        (
            "EUR",
            [],
        ),
    ],
)
def test_filter_by_currency(transactions: list[dict], currency: str, expected: list[dict]) -> None:
    result = list(filter_by_currency(transactions, currency))
    assert result == expected


# Тест функции, возвращающей описание транзакции
def test_transaction_description(transactions: list[dict]) -> None:
    result = list(transaction_descriptions(transactions))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
    ]
    assert result == expected


# тест функции, генерирующей 16-значный номер карты
def test_card_number_generator() -> None:
    result = list(card_number_generator(0, 999))
    expected = [
        f'{(f"{x:016}")[:4]} {(f"{x:016}")[4:8]} {(f"{x:016}")[8:12]} {(f"{x:016}")[12:]}' for x in range(1000)
    ]
    assert result == expected
