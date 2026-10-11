from datetime import datetime
from functools import wraps
from os import PathLike
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def log(filename: str | PathLike[str] | None = None) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Функция-декоратор, которая создает журнал вызовов функции.

    Аргументы:
        filename: Путь к файлу журнала или None для вывода в консоль.

    Возвращаемые значения:
        Декоратор для логирования вызовов функций.
    """

    def write_log(message: str) -> None:
        """Функция записи логов в файл или консоль."""
        if filename is None:
            print(message)
        else:
            with open(filename, "a", encoding="utf-8") as file:
                file.write(message + "\n")

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        """Функция-декоратор, которая принимает исходную функцию и оборачивает ее."""

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            """
            Функция-обертка для исходной функции.
            Записывает время начала вызова функции, логирует ошибку или успешное выполнение.
            """
            start_time = datetime.now()
            try:
                result = func(*args, **kwargs)
            except Exception as error:
                write_log(
                    f"{start_time} | {func.__name__} error: " f"{type(error).__name__}. Inputs: {args}, {kwargs}"
                )
                raise
            else:
                write_log(f"{start_time} | {func.__name__} ok")
                return result

        return wrapper

    return decorator
