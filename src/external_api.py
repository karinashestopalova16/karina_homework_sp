import os

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_transactions_to_rubles(transaction: dict) -> float | None:
    """
    Функция, которая принимает словарь с данными об операции
    и конвертирует сумму транзакции в рубли.
    """
    amount = transaction["operationAmount"]["amount"]
    code = transaction["operationAmount"]["currency"]["code"]
    if code == "RUB":
        return float(amount)

    api_key = os.getenv("EXCHANGE_RATES_API_KEY")
    if api_key is None:
        raise ValueError("EXCHANGE_RATES_API_KEY is not set")

    else:
        params = {
            "from": code,
            "to": "RUB",
            "amount": amount,
        }
        url = "https://api.apilayer.com/exchangerates_data/convert"
        headers = {"apikey": api_key}
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            data = response.json()
            return float(data["result"])
        except requests.exceptions.RequestException:
            print("An error occurred. Please try again later.")
            return None
