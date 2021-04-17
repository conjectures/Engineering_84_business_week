# Let's create tests to check if the code would be running without any errors

# Import unittest to inherit TestCase - use it to create tests against our code.
import unittest
# Import class to be tested
from simple_calc import SimpleCalc


class CalcTest(unittest.TestCase):

    calc = SimpleCalc()

    # Naming convention: 'test_' before name of the function
    def test_add(self):
        # Test if teh value of 2+4 is equal to 6 when using calc.add()
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_subtract(self):
        # Test if the value of 4-2 is equal to 2 when using calc.subtract()
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        # Test if the value of 2*2 is equal to 4 when using calc.multiply()
        self.assertEqual(self.calc.multiply(2, 2), 4)

    def test_divide(self):
        # Test if the value of 512/32 is equal to 16 when using calc.divide()
        self.assertEqual(self.calc.divide(512, 32), 16)
