import unittest
from src.homework.j_classes.class_a import Die

class TestDie(unittest.TestCase):
    def test_roll_values(self):
        die = Die()
        for _ in range(3):
            die.roll()
            roll_value = die.get_rolled_value()
            self.assertIn(roll_value, range(1,7), "Roll value is out of range")

    def test_str_method(self):
        die = Die()
        die.roll()
        expected_output = f"The rolled value is {die.get_rolled_value()}"
        self.assertEqual(str(die), expected_output, "String representation is incorrect")

#making sure it all gets commitemed at once