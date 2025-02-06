def main():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

def fizzbuzz():
    result = []
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            result.append("FizzBuzz")
        elif num % 3 == 0:
            result.append("Fizz")
        elif num % 5 == 0:
            result.append("Buzz")
        else:
            result.append(num)
    return result

import unittest

class TestFizzBuzz(unittest.TestCase):
    
    def test_fizzbuzz(self):
        result = fizzbuzz()
        self.assertEqual(len(result), 100)
        self.assertEqual(result[14], "FizzBuzz")
        self.assertEqual(result[2], "Fizz")
        self.assertEqual(result[4], "Buzz")
        self.assertEqual(result[0], 1)

if __name__ == '__main__':
    unittest.main()
