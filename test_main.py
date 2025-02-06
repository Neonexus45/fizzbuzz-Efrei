import unittest
from main import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_multiples_of_3(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(6), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")

    def test_multiples_of_5(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(20), "Buzz")
        self.assertEqual(fizzbuzz(25), "Buzz")

    def test_multiples_of_3_and_5(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")
        self.assertEqual(fizzbuzz(45), "FizzBuzz")

    def test_non_multiples(self):
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(7), "7")
        self.assertEqual(fizzbuzz(22), "22")

if __name__ == "__main__":
    unittest.main()