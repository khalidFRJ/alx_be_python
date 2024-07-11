import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(4, 3), 7, "should be true")

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(4, 3), 1, "should be true")

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 3), 12, "should be true")

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 3), 1.3333, places=4, msg="should be true")

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(1, 0)

if __name__ == '__main__':
    unittest.main()

