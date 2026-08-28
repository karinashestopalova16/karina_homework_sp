import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_valid_card_number() -> None:
    result = get_mask_card_number("7000792289606361")
    assert result == "7000 79** **** 6361"


def test_get_mask_another_card_number() -> None:
    result = get_mask_card_number("1234567890123456")
    assert result == "1234 56** **** 3456"


def test_get_mask_invalid_card_number() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("1234")


def test_get_mask_valid_account() -> None:
    result = get_mask_account("73654108430135874305")
    assert result == "**4305"


def test_get_mask_invalid_account() -> None:
    with pytest.raises(ValueError):
        get_mask_account("123")
