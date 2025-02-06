from fizzbuzz import fizzbuzz
import unittest

class TestFizzBuzz(unittest.TestCase):
    
    def test_fizzbuzz(self):
        result = fizzbuzz()
        self.assertEqual(len(result), 100)
        self.assertEqual(result[14], "FizzBuzz")
        self.assertEqual(result[2], "Fizz")
        self.assertEqual(result[4], "Buzz")
        self.assertEqual(result[0], 5)

if __name__ == '__main__':
    unittest.main()
()