from typing import Any
from unittest.mock import Mock, mock_open, patch

import pytest

from src.utils import get_operations_from_json


@pytest.mark.parametrize("data, expected", [("", []), ('{"state": }', [])])
def test_get_operations_from_json_incorrect_file(data: str, expected: list[dict[str, Any]]) -> None:
    mocked_open = mock_open(read_data=data)

    with patch("builtins.open", mocked_open):
        assert get_operations_from_json("fake_path.json") == expected


def test_get_operations_from_json_invalid_structure() -> None:
    mocked_open = mock_open(read_data="33")

    with patch("builtins.open", mocked_open):
        assert get_operations_from_json("fake_path.json") == []

        mocked_open.assert_called_once_with("fake_path.json", encoding="utf-8")


def test_get_operations_from_json_file_not_found() -> None:
    mocked_open = Mock(side_effect=FileNotFoundError)

    with patch("builtins.open", mocked_open):
        assert get_operations_from_json("fake_path.json") == []


def test_get_operations_from_json() -> None:
    mocked_open = mock_open(read_data='[{"state": "EXECUTED"}]')

    with patch("builtins.open", mocked_open):
        assert get_operations_from_json("fake_path.json") == [{"state": "EXECUTED"}]

        mocked_open.assert_called_once_with("fake_path.json", encoding="utf-8")
