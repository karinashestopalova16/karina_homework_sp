from unittest.mock import patch

import pytest
import requests

from src.external_api import convert_transactions_to_rubles


@pytest.fixture
def use_test_transaction() -> list[dict]:
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


# Тест функции конвертации суммы в рубли из рубли (возвращается изначальное значение и не происходит запроса API)
def test_convert_from_rub_to_rub(use_test_transaction: list[dict]) -> None:
    with patch("src.external_api.requests.get") as mock_get:
        result = convert_transactions_to_rubles(use_test_transaction[1])
        expected = 79114.93
        mock_get.assert_not_called()

    assert result == expected


# Тест функции конвертации суммы в рубли из другой валюты и запроса API
def test_convert_to_rub(use_test_transaction: list[dict]) -> None:
    with patch("src.external_api.os.getenv", return_value="test_api_key"):
        with patch("src.external_api.requests.get") as mock_get:
            mock_response = mock_get.return_value
            mock_response.json.return_value = {"result": 815390.8}

            result = convert_transactions_to_rubles(use_test_transaction[0])
            expected = 815390.8

            params = {
                "from": "USD",
                "to": "RUB",
                "amount": use_test_transaction[0]["operationAmount"]["amount"],
            }
            url = "https://api.apilayer.com/exchangerates_data/convert"
            headers = {"apikey": "test_api_key"}

            mock_get.assert_called_once_with(url, params=params, headers=headers)

        assert result == expected


# Тест функции конвертации суммы в рубли - обработка ошибки запроса
def test_convert_to_rub_request_error(use_test_transaction: list[dict]) -> None:
    with patch(
        "src.external_api.requests.get",
        side_effect=requests.exceptions.RequestException("An error occurred. Please try again later."),
    ):
        result = convert_transactions_to_rubles(use_test_transaction[0])

    assert result is None


# Тест функции конвертации суммы в рубли - отсуствие API-ключа
def test_convert_to_rub_without_api_key(use_test_transaction: list[dict]) -> None:
    with patch(
        "src.external_api.os.getenv",
        return_value=None,
    ):
        with pytest.raises(
            ValueError,
            match="EXCHANGE_RATES_API_KEY is not set",
        ):
            convert_transactions_to_rubles(use_test_transaction[0])
