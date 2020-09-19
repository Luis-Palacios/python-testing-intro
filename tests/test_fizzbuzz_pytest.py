import pytest
from utils.fizzbuzz import fizz_or_buzz, fizzbuzz_sequence


@pytest.mark.parametrize(
    "number,expected", [(1, 1), (3, "fizz"), (5, "buzz"), (15, "fizzbuzz")]
)
def test_fizz_or_buzz(number, expected):
    result = fizz_or_buzz(number)
    assert result == expected


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
