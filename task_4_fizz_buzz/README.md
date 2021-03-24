# TASK 4 - Fizz Buzz!

## Summary
Super simple game that will substitute multiples of 3 and 5 for fizz an buzz respectily, or fizzbuzz for multiples of the two

## Tasks
**_Core:_**
Write a program that prints the numbers from 1 to 100. For multiples of three print "Fizz" instead of the number
For the multiples of five print "Buzz" instead of the number For numbers which are multiples of both three and five print "FizzBuzz".

**_Extra:_**
make a new fizzbuzz file and make it functional make it so we we can decide which numbers to substitute for fizz and buzz using functions

*Hint*: loop, range, control flow


## Acceptance Criteria
- All core tasks are done
- Core tasks work without errors

## Documentation
Run program with `python main.py`

The program will ask for two numbers (smaller than 100) and will output your fizzbuzz!

## Solution
The challenge is solved with a function that takes two arbitrary numbers as input, as well as a max number for the fizzbuzz challenge.
```python
def fizzbuzz(numA, numB, maxnum):
    # create number list
    numbers = list(range(1, maxnum))
    # iterate through the numbers
    for i in numbers:
        # Check if number is modulo of number A or number B, and create an appropriate string
        temp = ('Fizz' if not i % numA else '') + ('Buzz' if not i % numB else '')
        if temp is not '':
            # Assign string to list with index i-1 (lists index from 0 while the numbers start from 1)
            numbers[i-1] = temp
    return numbers
```
The function then creates a list with numbers starting from 1 to `maxnum` and iterates through them to find if they are 
divisible with `numA`, `numB` or both.

A string is created that stores the values *Fizz*, *Buzz* or *FizzBuzz* appropriately, and then stores it to the numbers list
after checking.

The program then returns the list with the numbers to be printed
