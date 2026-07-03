import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 20), 30)

    def test_add_negative(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-10, -20), -30)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, -5), -5)

if __name__ == '__main__':
    unittest.main()
