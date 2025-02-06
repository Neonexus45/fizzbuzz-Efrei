import unittest
import main

class TestFizzBuzz(unittest.TestCase):

    def multiple_3(self):
        self.assertEqual(main.fizzbuzz(3), "Fizz")
        self.assertEqual(main.fizzbuzz(6), "Fizz")
        self.assertEqual(main.fizzbuzz(9), "Fizz")

    def multiple_5(self):
        self.assertEqual(main.fizzbuzz(5), "Buzz")
        self.assertEqual(main.fizzbuzz(10), "Buzz")
        self.assertEqual(main.fizzbuzz(20), "Buzz")

    def multiple_3_and_5(self):
        self.assertEqual(main.fizzbuzz(15), "FizzBuzz")
        self.assertEqual(main.fizzbuzz(30), "FizzBuzz")
        self.assertEqual(main.fizzbuzz(45), "FizzBuzz")

    def not_multiple_3_et_5(self):
        self.assertEqual(main.fizzbuzz(1), 1)
        self.assertEqual(main.fizzbuzz(2), 2)
        self.assertEqual(main.fizzbuzz(4), 4)

if __name__ == "__main__":
    unittest.main()