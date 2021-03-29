# Python Test Driven Development

## Why should we use TDD
## What are the benefits of using TDD

### Best use cases
- We will use pytest unit test in Python to implement TDD
- TDD is widely used sand is the cheapest way to test the code or implement test deiven development.

![TDD Diagram](TDD.png)

**Best practices for TDD**
- Write the smalles possible test case that mathces what we need to program
- TDD cycle starts with everything failing: `RED`
- Write code to pass the test: `GREEN`
- Refator the code for next test `Blue`
- This continues untill all the tests have successfully passed

|Method |   Checks that|   New in |
|:---|:---|:---|
|assertEqual(a, b)        | a == b              ||
|assertNotEqual(a, b)     |    a != b              ||  
|assertTrue(x)            |    bool(x) is True     ||  
|assertFalse(x)           |    bool(x) is False    ||  
|assertIs(a, b)           |    a is b             |3.1|
|assertIsNot(a, b)        |    a is not b          |3.1|
|assertIsNone(x)          |    x is None           |3.1|
|assertIsNotNone(x)       |    x is not None       |3.1|
|assertIn(a, b)           |    a in b              |3.1|
|assertNotIn(a, b)        |    a not in b         |3.1|
|assertIsInstance(a, b)   |    isinstance(a, b)    |3.2|
|assertNotIsInstance(a, b)|    not isinstance(a,b) |3.2|

- Let's create a file called `test_unittest_simplecalc.py`
- Naming convention is extremely important when it comes to testing in Python

```python
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
```
Run python tests with `python -m pytest`. Evidently, the tests will fail.
We continue by writing the simplest code required for the tests to succeed.
```python
class SimpleCalc:

    def add(self, value1, value2):
        return value1 + value2

    def subtract(self, value1, value2):
        return value1 - value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        return value1 / value2
```
Running `python -m pytest` again, pytest will succeed with 4 tests passed:
```bash
============================================== test session starts ===============================================
platform linux2 -- Python 2.7.17, pytest-4.6.11, py-1.10.0, pluggy-0.13.1
rootdir: /home/alex/docs/edu/spg/py_week_02/day-01/eng84_python_tdd
collected 4 items

test_unittest_simplecalc.py ....                                                                           [100%]

============================================ 4 passed in 0.03 seconds ============================================
```
## Pytest and Unittest
The module `pytest` looks for any file with a name that includes the pattern `test*.py`. It uses `unittest` to perform tests.
We can use `unittest` directly with `python -m unittest discover -v`
`pytest` offers a more readable form when using the flag `-v` for verbose:
```bash
$ python -m pytest -v
[...]
collected 4 items

test_unittest_simplecalc.py::CalcTest::test_add PASSED                                                     [ 25%]
test_unittest_simplecalc.py::CalcTest::test_divide PASSED                                                  [ 50%]
test_unittest_simplecalc.py::CalcTest::test_multiply PASSED                                                [ 75%]
test_unittest_simplecalc.py::CalcTest::test_subtract PASSED                                                [100%]

============================================ 4 passed in 0.02 seconds ============================================
```
