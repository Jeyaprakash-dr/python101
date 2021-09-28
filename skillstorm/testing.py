# Built in module
import unittest

from skillstorm.calculator import Calculator


class CalculatorTest(unittest.TestCase):

    def test_add(self):
        one = 10
        two = 5
        expected_result = 15
        actual_result = Calculator().add(one, two)

        # if the method does not return the expected result, Fail the test
        self.assertEqual(expected_result, actual_result)

    def test_negative(self):
        one = -5
        two = 10
        expected = 5
        actual = Calculator().add(one, two)

        self.assertEqual(expected, actual)

    def test_multiply(self):
        expected = 50
        actual = Calculator().multiply(5, 10)
        self.assertEqual(expected, actual)
