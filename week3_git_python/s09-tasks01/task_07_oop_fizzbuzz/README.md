# TASK 7 - OOP Fizz Buzz!

## Summary
Super simple game that will substitute multiples of 3 and 5 for fizz an buzz respectily, or fizzbuzz for multiples of the two, now with the use of
Object Oriented Programming.

## Tasks
Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”."

*Note: Must be in class-method format*

## Acceptance Criteria
- All tasks are done
- Core tasks work without errors

## Documentation

### Running the program
Run program with `python main.py`

### How to import
To use the library, import the file. In the file, the class `FizzBuzz()` is available.
The class when initialised can receive a positional argument to change the max number of numbers for the fizzbuzz challenge.

### How to use class
After the class is instantiated, the fizzbuzz is calculated by calling the method `fizzbuzzify`.
The method `fizzbuzzify` takes two positional arguments for the numbers that will fizz or buzz accordingly.
The numbers can be either in the form of an integer or as a string. This means, the class will automatically handle
user input as the numbers for the fizzbuzz without additional checking from the user.
When the fizzbuzz is calculated it will be printed automatically for the user.

If the user wants to view the numbers again, the method `show_numbers` can be used to do so.

To try another fizzbuzz combination, the object number list needs to be reset. The method `reset_numbers` is provided for this reasen.
Therefore, before running `fizzbuzzify` again, the method `reset_numbers` has to be executed.

## Solution
The program is written in OOP. That is, the fizzbuzz is calculated with the use of a class. 

When a class is instantiated, the initialisation method `__init__` will set the attribute of `maxnum` and will then create a list of numbers from the range 1 to `maxnum`.


```python
class FizzBuzz():

    def __init__(self, maxnum=100):
        self.maxnum = maxnum
        self.numbers = list(range(1, maxnum))
```

The class gets the numbers for *fizz* and *buzz* as inputs, and wil therefore require special methods that can handle those inputs.
The inputs can either be in the form of a string, or directly as integers. The mehtod `_check_number` is the internal method that handles these problems.

In short, the method takes a value, checks if it is a digit or an integer and then checks if the number is within the bounds of 0 and `maxnum`.
If any of these checks fail, a `False` value is returned.

However, the `isdigit` method is only available for strings. 
To circumvent this, a try-except block is used so that if an integer is passed, the bounds check is still performed.
```python
    # Check if the numbers that were given are positive and nonzero
    def _check_number(self, value):
        try:
            if value.isdigit():
                # Cast to integer then perform the bound check
                return self._num_in_bounds(int(value))
            return False
        # Except an AttributeError if the value is an integer
        except AttributeError:
            return self._num_in_bounds(value)
```

The bounds check is performed by a different internal method, shown below.
This method, `_num_in_bounds` will always receive a number value as input.
If the number is a `float` or `decimal`, the check will succeed.
```python
    # Check if a number is within bounds (between 0 and maxnum)
    def _num_in_bounds(self, number):
        if number > 0 and number < self.maxnum:
            return True
        return False
```

The `fizzbuzzify` method is where the fizzbuzz quiz is calculated.
After the checks are performed, the numbers are floored to the nearest integer and saved as attributes.
Then, a list traversal goes through every number in the `numbers_list` of the class and checks if the current number is divisible by the two numbers.
If it is divisible by the first number, the word *Fizz* is appended to a temporary string. If it is divisible by the second number, the word *Buzz* is appended instead. 
Therefore, if it is divisible by the two, the word *FizzBuzz* is formed.
Finally, the temporary string is assigned to the current number in the `numbers_list`. When the list traversal is complete, the full list is printed for the user.
```python
    def fizzbuzzify(self, numA=3, numB=5):
        if not (self._check_number(numA) and self._check_number(numB)):
            print('Wrong inputs, cancelling operation')
            return
        self.numA = int(numA)
        self.numB = int(numB)

        for idx in self.numbers:
            temp = ('Fizz' if not idx % self.numA else '') + ('Buzz' if not idx % self.numB else '')
            # check if temp is empty
            if temp:
                self.numbers[idx-1] = temp
        self.show_numbers()
```

There printing of the `numbers_list` list is handled by the method below. It iterates throught the list and prints each item in a separate line.
```python
    def show_numbers(self):
        for items in self.numbers:
            print(items)
```
