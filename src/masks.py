import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOGS_DIR = BASE_DIR / "logs"
LOGS_DIR.mkdir(exist_ok=True)


# Создаем объект логера
logger = logging.getLogger(__name__)

# Создаем обработчик для вывода логов в файл и форматер
file_handler = logging.FileHandler(LOGS_DIR / "masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(module)s %(levelname)s: %(message)s")

# Передаем хэндлеру форматер
file_handler.setFormatter(file_formatter)

# Передаем логеру хэндлер
logger.addHandler(file_handler)

# Устанавливаем уровень сообщения
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает номер карты и маскирует ее"""
    if len(card_number) != 16:
        logger.error("Маскировка карты не выполнена - некорректный номер карты.")
        raise ValueError("Некорректный номер карты.")

    logger.info("Номер карты успешно замаскирован.")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """Функция, которая принимает номер счета и маскирует его"""
    if len(account) < 4:
        logger.error("Маскировка счета не выполнена - некорректный номер счета.")
        raise ValueError("Некорректный номер счета.")

    logger.info("Номер счета успешно замаскирован.")
    return f"**{account[-4:]}"
