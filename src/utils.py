import json
import logging
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent.parent
LOGS_DIR = BASE_DIR / "logs"
LOGS_DIR.mkdir(exist_ok=True)


# Создаем объект логера
logger = logging.getLogger(__name__)

# Создаем обработчик для вывода логов в файл и форматер
file_handler = logging.FileHandler(LOGS_DIR / "utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(module)s %(levelname)s: %(message)s")

# Передаем хэндлеру форматер
file_handler.setFormatter(file_formatter)

# Передаем логеру хэндлер
logger.addHandler(file_handler)

# Устанавливаем уровень сообщения
logger.setLevel(logging.DEBUG)


def get_operations_from_json(file_path: str) -> list[dict[str, Any]]:
    """
    Функция, которая принимает путь к файлу, читает его
    и возвращает список словарей с данными о финансовых операциях.
    """
    try:
        with open(file_path, encoding="utf-8") as f:  # Открываем файл
            operations = json.load(f)  # Читаем файл
    except json.JSONDecodeError:  # Обрабатываем ошибку чтения JSON-файла
        logger.error("Некорректный JSON-файл: не удалось разобрать содержимое файла.")
        return []
    except FileNotFoundError:  # Обрабатываем ошибку - файл не найден по заданному пути
        logger.error("Файл не найден.")
        return []
    # Если файл не пуст и найден, проверяем два условия - operations это список, а внутри него словари
    if isinstance(operations, list) and all(isinstance(operation, dict) for operation in operations):
        logger.info("JSON-файл успешно прочитан, структура данных корректна.")
        return operations  # Возвращаем, если оба условия соблюдены
    else:
        logger.error("Некорректная структура данных: ожидался список словарей.")
        return []  # Возвращаем пустой список, если хотя бы одно условие не истина
