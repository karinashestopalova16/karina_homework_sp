import pytest

from src.widget import get_date, mask_account_card


# тест маскировки карты или счета
@pytest.mark.parametrize(
    "card_or_account_number, expected",
    [
        ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
        ("Счет 12345678901234567890", "Счет **7890"),
        ("MasterCard 1234567890123456", "MasterCard 1234 56** **** 3456"),
    ],
)
def test_mask_account_card(card_or_account_number: str, expected: str) -> None:
    result = mask_account_card(card_or_account_number)
    assert result == expected


# тест выбрасывания ошибки при некорректном вводе карты или счета
@pytest.mark.parametrize("invalid_acc_card_input", ["Visa", "", "Visa Super Card 1234 5678"])
def test_invalid_account_card_mask(invalid_acc_card_input: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(invalid_acc_card_input)


# тест функции перевода даты в формат ДД.ММ.ГГГГ
@pytest.mark.parametrize(
    "iso_format, expected",
    [
        ("2024-03-15T12:30:00", "15.03.2024"),
        ("2023-11-07T08:15:00", "07.11.2023"),
        ("2024-01-01T00:00:00", "01.01.2024"),
    ],
)
def test_get_date(iso_format: str, expected: str) -> None:
    result = get_date(iso_format)
    assert result == expected


# тест выбрасывания ошибки при некорректном вводе даты формата ISO
@pytest.mark.parametrize("invalid_iso_date", ["", "2024-13-15", "2024.03.15.", "дата"])
def test_invalid_date_format(invalid_iso_date: str) -> None:
    with pytest.raises(ValueError):
        get_date(invalid_iso_date)
