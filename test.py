import unittest;
from main import fizzbuzz;

class TestFizzbuzz(unittest.TestCase):
    def test_isFizz(self):
        fizzbuzz(3)
        self.assertEqual(fizzbuzz(3), "fizz")
    def test_isBuzz(self):
        fizzbuzz(5)
        self.assertEqual(fizzbuzz(5), "buzz")
    def test_isFizzbuzz(self):
        fizzbuzz(15)
        self.assertEqual(fizzbuzz(15), "fizz")
    def test_isNumber(self):
        fizzbuzz(1)
        self.assertEqual(fizzbuzz(1), "1")

if __name__ == '__main__':
    unittest.main()
