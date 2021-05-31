# Task 1: TDD Bread Factory
> Time: 30-45 Minutes

## Summary
TDD bread factory is the latest bread brand in Py Land.
It always produces the best bread because it has the best testing strategy!
What they do is before they make any new bread, they make a test to make sure the end ouput is correct.
Then they adjust the recipe until it's just right!

You are going to do the same with bread! This is called Test Driven Development.

## Tasks
This exercise is going to bring together lots of concepts.
### Learning Outcomes
- Git & Github
- Functions
- TDD
- Separation of concerns (important do not ignore!)
- DRY code
- DOD (Definition of Done)

### Intalling and running
To run the naan factory do the following:

- Import naan_factory
- run_factory()
- Use TDD - test driven development
- Write the test
- Run it, and read the error
- Code and make it pass the test

This helps with:
- Stop over engineering
- Maintainable code
- Reduce technical debt
- Goes well with agile and working code
- errors can be your guide in complex systems

How it works: write unit tests.

Unit Tests
Test single pieces of code. Like a function.

### Base of a test
Usually has 3 phases.
- Setup phase (know variables)
- Calling of the function / piece of code with know variables
- Asserting for expect output

## User stories for Naan Factory
1. As a user, I can use the make dough with 'water' and 'flour' to make 'dough'.
2. As a user, I can use the bake dough with 'dough' to get naan.
3. As a user, I can use the run factory with water and flour and get naan.

## Acceptance Criteria
- You have written tests
- Test pass
- You have written more test to make sure everything works as indented
- All user stories are satisfied
- Code does not break
- Code has exit condition
- DOD if followed

## Solution
To solve this task using TDD, we look at the User Stories, and try to implement them with the test cases.
First, the appropriate functions are created in the `naan_factory.py` file:
```python
make_dough(*args):
  pass

bake_dough(*args):
  pass

fun_factory(*args):
  pass
```
Then, while importing the functions in the `test_naan_factory.py` file, we create a class from the `unittest`  module to test the different cases.

```python
import unittest
import naan_factory as nf

class FactoryTest(unittest.TestCase):

    # Test if adding 'water' and 'flour' in the 'run_factory' function will create 'naan'
    def test_run_factory(self):
        self.assertEqual(nf.run_factory('water', 'flour'), 'naan')

    # Test if adding 'water' and something other than 'flour' in the 'run_factory' function will create give None
    def test_run_factory_wrong_inputs(self):
        self.assertIsNone(nf.run_factory('water', 'else'))

    # Test if adding 'water' and 'flour' with swithced positions in the 'run_factory' function will create 'naan'
    def test_run_factory_switch_inputs(self):
        self.assertEqual(nf.run_factory('flour', 'water'), 'naan')

    # Test if adding 'water' and 'flour' in the 'make_dough' function will produce 'flour'
    def test_make_dough(self):
        self.assertEqual(nf.make_dough('water', 'flour'), 'dough')

    # Test if adding 'flour' 'bake_dough' function will produce 'naan'
    def test_bake_dough(self):
        self.assertEqual(nf.bake_dough('dough'), 'naan')
```
Some additional assertions are made, to makes sure that the users have a better experience. Mainly, we test if passing a different input will give `None` as input, or if the user gives the right inputs in the wrong order, the program will still execute correctly.

When we test the above test file, we will get 5 failures, however, there are no syntax errors yet, which is reassuring.
Next, the functions will be 'filled' such that the test succeed.
Starting from `make_dough`, we make a function that takes a number of arguments (for flexibility). Then, we check if the number of arguments passed, is the right amount.
After, that, we check if the ingredients that were given are the correct ones, in either order. If all those conditions are met, then the string 'dough' is returned:
```python
def make_dough(*args):
    # Check if 2 ingredients were passed
    if len(args) == 2:
        # Check if the ingredients that were passed are exactly 'water' and 'flour' in any order.
        if args[0] in ['water', 'flour'] and args[1] in ['water', 'flour'] and args[0] != args[1]:
            return 'dough'
```
For the `bake_dough` function, we only need to check if one arguments was passed, and if that argument is dough. The resulting string is 'naan' as described in the user stories.
```python
def bake_dough(*args):
    # Check if only one ingredient is passed
    if len(args) == 1:
        # Check if that ingredient is 'dough'
        if args[0] == 'dough':
            return 'naan'
```
Finally, for the `run_factory` function, we use the above two functions in conjunction, to get the desired result.
```python
def run_factory(*args):
    # Call make_dough to pass ingredients to bake_dough. Return result
    return bake_dough(make_dough(*args))
```
As we need to satisfy the user stories, we need to make an interface so that users can utilise the above code. For this reason, the `main` function was created:
```python
def main():
    while True:
        # ASsk for user choice to continue or exit
        choice = input("Run factory? [y/n]")
        # Check user choice
        if choice.lower() in ['y', 'yes']:
            # Ask for ingredients
            ingredient_01 = input("Ingredient 1? \n")
            ingredient_02 = input("Ingredient 2? \n")
            result = run_factory(ingredient_01, ingredient_02)
            # Check if resutl is not None
            if result:
                print(f'You get {result}!\n\n')
            # If result is none, print failure message
            else:
                print('You failed to make bread\n\n')
        # Handle exit condition
        elif choice.lower() in ['n', 'no']:
            print('Goodbye!\n')
```
The main function starts with a `while` loop that executes until the user enters 'n' or 'no' in the upcoming question. If the user chooses to continue,
he should input 'y' or 'yes'. When the program is set to continue, it will ask the user for two strings, representing the first and second ingredients that will be passed to the `run_factory` function.
If the user passes the right ingredients, the factory will function as stated in the product requirements.

If the tests are checked once again, the developed code will succeed in all 5 checks:
```bash
============================================== test session starts ===============================================
[...]
collected 5 items

test_naan_factory.py::FactoryTest::test_bake_dough PASSED                                                  [ 20%]
test_naan_factory.py::FactoryTest::test_make_dough PASSED                                                  [ 40%]
test_naan_factory.py::FactoryTest::test_run_factory PASSED                                                 [ 60%]
test_naan_factory.py::FactoryTest::test_run_factory_switch_inputs PASSED                                   [ 80%]
test_naan_factory.py::FactoryTest::test_run_factory_wrong_inputs PASSED                                    [100%]

=============================================== 5 passed in 0.03s ================================================
```
