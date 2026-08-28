import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_number: str) -> str:
    """Функция, которая маскирует номер карты или счета"""
    parts = card_or_account_number.split()

    if len(parts) < 2 or len(parts) > 3:
        raise ValueError("Некорректный ввод")

    number_to_mask = parts[-1]

    if parts[0].lower() == "счет":
        return f"{parts[0].capitalize()} {get_mask_account(number_to_mask)}"

    return f"{' '.join(parts[:-1])} {get_mask_card_number(number_to_mask)}"


def get_date(date_to_change: str) -> str:
    """Функция, которая возвращает дату в формате ДД.ММ.ГГГГ"""
    final_date = datetime.datetime.fromisoformat(date_to_change)

    return final_date.strftime("%d.%m.%Y")
