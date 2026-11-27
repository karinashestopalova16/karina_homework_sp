import pandas as pd


def read_csv_file(file_path: str) -> list[dict]:
    """Функция, которая читает операции из CSV-файла"""

    df = pd.read_csv(file_path, sep=";")
    return df.to_dict("records")


def read_excel_file(file_path: str) -> list[dict]:
    """Функция, которая читает операции из EXCEL-файла"""

    df = pd.read_excel(file_path)
    return df.to_dict("records")
