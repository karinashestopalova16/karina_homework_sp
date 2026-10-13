import pytest
from src.decorators import log


def test_log_success(capsys):
    @log()
    def my_function(x, y):
        return x + y
    result = my_function(2, 4)
    assert result == 6
    captured = capsys.readouterr()
    assert "my_function ok" in captured.out


def test_log_error(capsys):
    @log()
    def divide_func(x, y):
        return x / y
    with pytest.raises(ZeroDivisionError):
        divide_func(2, 0)
    captured = capsys.readouterr()
    assert "divide_func error" in captured.out
    assert "ZeroDivisionError" in captured.out


def test_log_file(tmp_path):
    log_file = tmp_path / "test.log"
    @log(log_file)
    def my_function(x, y):
        return x + y
    result = my_function(2, 1)
    assert result == 3
    content = log_file.read_text(encoding="utf-8")
    assert "my_function ok" in content
