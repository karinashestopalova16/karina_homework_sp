def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает номер карты и маскирует ее"""
    if len(card_number) != 16:
        raise ValueError("Некорректный номер карты")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """Функция, которая принимает номер счета и маскирует его"""
    if len(account) < 4:
        raise ValueError("Некорректный номер счета")

    return f"**{account[-4:]}"
