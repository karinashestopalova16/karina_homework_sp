import pytest

from src.masks import get_mask_account, get_mask_card_number


# тест маскировки номера карты
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456"),
    ],
)
def test_card_mask(card_number: str, expected: str) -> None:
    result = get_mask_card_number(card_number)
    assert result == expected


# тест выбрасывания ошибки при некорректном вводе номера карты
@pytest.mark.parametrize("invalid_card_number", ["1234", "", "12345678912345678912345"])
def test_invalid_card_mask(invalid_card_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_card_number)


# тест маскировки номера счета
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("1234", "**1234"),
    ],
)
def test_get_account_mask(account_number: str, expected: str) -> None:
    result = get_mask_account(account_number)
    assert result == expected


# тест выбрасывания ошибки при некорректном вводе номера счета
@pytest.mark.parametrize("invalid_account_number", ["123", ""])
def test_invalid_account_number_mask(invalid_account_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_account(invalid_account_number)
