import unittest
from src.badge_junkie.math_utils import factorial


class TestMathUtils(unittest.TestCase):

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)

    def test_factorial_invalid_input(self):
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(3.5)
        with self.assertRaises(ValueError):
            factorial("five")


if __name__ == "__main__":
    unittest.main()
