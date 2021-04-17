# Python Test Driven Development

## What is Test Driven Development
Test Driven Development is a software development process that involves writing tests that check certain functionality of the product, before writing the production code.
After a unit test is added, the programmers write just the simplest code possible and trial it against the unit test. If the test passes successfully, another unit test can be added for other functionalities, otherwise the code should be refactored.

The purpose of TDD is to help developers think more clearly about the requirements of the product.
Additionally, TDD has many benefits. It carries all the merits of iterative approaches, like reducing complexity, and is very well suited in Agile environments.
Unit tests are also used for validation, making sure that future changes do not affect the performance of the end product.

## TDD in Python
To demonstrate TDD of software, we use Python and its in-built module `pytest`.

### Test Driven Development life cycle
1. Write a test case that matches program requirements.
2. Run the tests. TDD cycles typically start with all test failing.
3. Write the simplest code to pass a test.
4. If the test does not succeed, refactor the code again until it passes the check.
5. Repeat cycle until all the functionality of the product is completed.

![TDD Diagram](TDD.png)


### Methods used in Python test
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

### TDD Example in Python
Let's create a file called `test_unittest_simplecalc.py`.

> Naming convention is extremely important when it comes to testing in Python. 
> This is because the `pytest` module searches for files that start with `test` to compile the unit tests.

In the file we have added the code seen below.
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
We can run the above tests with `python -m pytest`. Evidently, the tests will fail.
We continue by writing the simplest code required for the tests to succeed.


In a file named `simplecalc.py` we add the following functionality:
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
