import unittest
from calculator import subtract

class TestCalculator(unittest.TestCase):
    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-10, -5), -5)

    def test_subtract_zero(self):
        self.assertEqual(subtract(10, 10), 0)

    def test_subtract_large_numbers(self):
        self.assertEqual(subtract(1000000, 500000), 500000)

if __name__ == '__main__':
    unittest.main()
