import pytest
from functions import is_valid_imei

# Тестирование корректного IMEI
@pytest.mark.parametrize("imei", [
    ("490154203237518"),  # действительный IMEI
    ("987654321098765")   # недействительный IMEI
])
def test_valid_imei(imei):
    assert is_valid_imei(imei) is True

# Тестирование некорректных IMEI
@pytest.mark.parametrize("imei", [("37452749202940"),  # IMEI слишком короткий
                                  ("490154203237519"),  # Неверная контрольная цифра
                                  ("49015420323751A"),  # Нецифровой символ
                                  ("1234567890123A5")  # Нецифровой символ
])
def test_invalid_imei(imei):
    assert is_valid_imei(imei) is False
