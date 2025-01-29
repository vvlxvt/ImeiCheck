import pytest
from main import is_valid_imei

# Тестирование корректного IMEI
@pytest.mark.parametrize("imei", [
    ("490154203237518"),  # действительный IMEI
    ("123456789012345")   # недействительный IMEI
])
def test_valid_imei(imei):
    assert is_valid_imei(imei) is True

# Тестирование некорректных IMEI
@pytest.mark.parametrize("imei", [
    ("12345678901234"),   # IMEI слишком короткий
    ("490154203237519"),  # Неверная контрольная цифра
    ("49015420323751A"),  # Нецифровой символ
    ("1234567890123A5")   # Нецифровой символ в последней цифре
])
def test_invalid_imei(imei):
    assert is_valid_imei(imei) is False
