import unittest
from calculator import subtract

class TestCalculator(unittest.TestCase):
    def test_subtract_positive(self):
        self.assertEqual(subtract(10, 3), 7)

    def test_subtract_negative(self):
        self.assertEqual(subtract(-5, -2), -3)

    def test_subtract_zero(self):
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(5, 5), 0)
