import math
import unittest

def find_square_root(number):
    if number < 0:
        return "Square root of a negative number is undefined."
    else:
        return math.sqrt(number)

def cube(n):
    return n ** 3

class SquareRootTestCase(unittest.TestCase):
    def test_positive_number(self):
        result = find_square_root(16)
        self.assertAlmostEqual(result, 4)

    def test_zero(self):
        result = find_square_root(0)
        self.assertAlmostEqual(result, 0)

    def test_negative_number(self):
        result = find_square_root(-16)
        self.assertEqual(result, "Square root of a negative number is undefined.")


if __name__ == '__main__':
    unittest.main()
