import pytest
from utils.fizzbuzz import fizz_or_buzz, fizzbuzz_sequence


def test_fizz_or_buzz_number():
    number = 1
    result = fizz_or_buzz(number)
    assert number == result


def test_fizz_or_buzz_fizz():
    number = 3
    result = fizz_or_buzz(number)
    assert result == "fizz"


def test_fizz_or_buzz_buzz():
    number = 5
    result = fizz_or_buzz(number)
    assert result == "buzz"


def test_fizz_or_buzz_fizzbuzz():
    number = 15
    result = fizz_or_buzz(number)
    assert result == "fizzbuzz"


def test_fizzbuzz_secuence():
    limit = 15
    result = fizzbuzz_sequence(limit)
    assert len(result) == limit
    assert result[0] == 1
    assert result[2] == "fizz"
    assert result[4] == "buzz"
    assert result[14] == "fizzbuzz"


def test_fizzbuzz_secuence_with_invalid_limit():
    limit = -1
    with pytest.raises(ValueError):
        fizzbuzz_sequence(limit)
