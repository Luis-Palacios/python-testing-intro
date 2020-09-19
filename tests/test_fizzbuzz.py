from unittest import TestCase
from utils.fizzbuzz import fizz_or_buzz, fizzbuzz_sequence


class TestFizzBuzz(TestCase):
    def test_number(self):
        number = 1
        result = fizz_or_buzz(number)
        self.assertEqual(number, result)

    def test_fizz(self):
        number = 3
        result = fizz_or_buzz(number)
        self.assertEqual(result, "fizz")

    def test_buzz(self):
        number = 5
        result = fizz_or_buzz(number)
        self.assertEqual(result, "buzz")

    def test_fizzbuzz(self):
        number = 15
        result = fizz_or_buzz(number)
        self.assertEqual(result, "fizzbuzz")

    def test_fizzbuzz_secuence(self):
        limit = 15
        result = fizzbuzz_sequence(limit)
        self.assertEqual(len(result), limit)
        self.assertEqual(result[0], 1)
        self.assertEqual(result[2], "fizz")
        self.assertEqual(result[4], "buzz")
        self.assertEqual(result[14], "fizzbuzz")

    def test_fizzbuzz_secuence_with_invalid_limit(self):
        limit = -1
        with self.assertRaises(ValueError):
            fizzbuzz_sequence(limit)
