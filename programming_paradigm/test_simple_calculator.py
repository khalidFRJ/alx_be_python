import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
     
     def test_addition(self):
          self.assertEqual( 4 + 3 , 7 , "shoold be true ")

     def test_subtraction(self):
          self.assertEqual( 4 - 3 , 1 , "shoold be true ")


     def test_multiply(self):
          self.assertEqual( 4 * 3 , 12 , "shoold be true ")


     def test_divide(self):
          self.assertEqual( 4 / 3 , 1.3333 , "shoold be true ")
          