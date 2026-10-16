# test_leap.py
from leap import is_leap

#Step 0.1: Your first test
def test_2024_is_a_leap_year():
    assert is_leap(2024) # Check a condition

#Step 0.2: Reading a failure report
def test_1900_is_not_a_leap_year():
    assert not is_leap(1900)
import pytest

#Step 0.3: One test, many inputs
@pytest.mark.parametrize("year, expected", [
    (2000, True),   # divisible by 400
    (1900, False),  # divisible by 100 but not by 400
    (2024, True),   # divisible by 4 but not by 100
    (2023, False),  # not divisible by 4
    (2400, True),   # divisible by 400 (our custom case 1)
    (2025, False),  # not divisible by 4 (our custom case 2)
])
def test_is_leap(year, expected):
    assert is_leap(year) == expected

#Step 0.4: Testing exceptions
def test_year_zero_is_rejected():
    with pytest.raises(ValueError, match="1 or later"):
        is_leap(0)

def test_negative_year_is_rejected():
    with pytest.raises(ValueError, match="1 or later"):
        is_leap(-100)

#Step 0.5: Fixtures for fresh test data
