import unittest
from hello import Calculator  

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up a Calculator instance for all test cases."""
        self.calc = Calculator()

    def test_add(self):
        """Test the add method."""
        result = self.calc.add(3, 5)
        self.assertEqual(result, 8)
        result = self.calc.add(-1, 1)
        self.assertEqual(result, 0)
        result = self.calc.add(-2, -2)
        self.assertEqual(result, -4)

    def test_subtract(self):
        """Test the subtract method."""
        result = self.calc.subtract(10, 5)
        self.assertEqual(result, 5)
        result = self.calc.subtract(0, 5)
        self.assertEqual(result, -5)
        result = self.calc.subtract(-1, -1)
        self.assertEqual(result, 0)

    def test_multiply(self):
        """Test the multiply method."""
        result = self.calc.multiply(3, 4)
        self.assertEqual(result, 12)
        result = self.calc.multiply(-1, 5)
        self.assertEqual(result, -5)
        result = self.calc.multiply(0, 100)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()