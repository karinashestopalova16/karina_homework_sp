from unittest.mock import Mock, patch

from src.file_readers import read_csv_file, read_excel_file


def test_read_csv_file() -> None:
    """Тестовая функция, проверяющая чтение CSV-файла"""

    expected_data = [{"id": 1, "amount": 500}]

    mock_df = Mock()
    mock_df.to_dict.return_value = expected_data

    with patch("src.file_readers.pd.read_csv", return_value=mock_df) as mock_read_csv:
        result = read_csv_file("transactions.csv")

    assert result == expected_data
    mock_read_csv.assert_called_once_with("transactions.csv", sep=";")
    mock_df.to_dict.assert_called_once_with("records")


def test_read_excel_file() -> None:
    """Тестовая функция, проверяющая чтение EXCEL-файла"""

    expected_data = [{"id": 1, "amount": 500}]

    mock_df = Mock()
    mock_df.to_dict.return_value = expected_data

    with patch("src.file_readers.pd.read_excel", return_value=mock_df) as mock_read_excel:
        result = read_excel_file("transactions_excel.xlsx")

    assert result == expected_data
    mock_read_excel.assert_called_once_with("transactions_excel.xlsx")
    mock_df.to_dict.assert_called_once_with("records")
