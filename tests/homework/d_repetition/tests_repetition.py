import unittest
from src.homework.d_repetition.repetition import get_factorial
from src.homework.d_repetition.repetition import sum_odd_numbers

class Test_Config(unittest.TestCase):
    def test_get_factorial(self):
        self.assertEqual(24, get_factorial(4))

    def test_get_factorial(self):
        self.assertEqual(120, get_factorial(5))

    def test_get_factorial(self):
        self.assertEqual(720, get_factorial(6))
    
    
    def test_sum_odd_numbers(self):
        self.assertEqual(16, sum_odd_numbers(7))
    
    def test_sum_odd_numbers(self):
        self.assertEqual(25, sum_odd_numbers(9))    
    
    def test_sum_odd_numbers(self):
        self.assertEqual(25, sum_odd_numbers(10))
