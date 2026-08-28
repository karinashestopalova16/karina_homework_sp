from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_number: str) -> str:
    """Функция, которая маскирует номер карты или счета"""
    parts = card_or_account_number.split()
    number_to_mask = parts[-1]

    if parts[0].lower() == "счет":
        return f"{parts[0]} {get_mask_account(number_to_mask)}"

    else:
        return f"{' '.join(parts[:-1])} {get_mask_card_number(number_to_mask)}"


def get_date(date_to_change: str) -> str:
    """Функция, которая возвращает дату в формате ДД.ММ.ГГГГ"""
    date_parts = date_to_change.split("T")
    date = date_parts[0]
    final_date = ".".join(date.split("-")[::-1])

    return final_date
