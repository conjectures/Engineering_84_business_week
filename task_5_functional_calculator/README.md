# TASK 5 - Functional Calculator

## Summary
Amazing you now know functions, lets make a functional calculator.

## Objectives
- Practice using, defining and calling functions
- Build a basic functional calculator

## Tasks
**_Core:_**
1. Build a function containing:
  - Add
  - Subtract
  - Multiply
  - Divide

2. Buld more functions for 
  - Area of a circle
  - Area of a square
  - Area of a triangle

**_Extra:_**
- Run function with arguments
- Assert against known values. Adding 10+30 will alwyas be 40
```python
# example
def add_function(arg1, arg2):
  return arg1 + arg2


print("calling the add_function() with 290 and 10, expect 300 to be the result ")
print(add_funtion(290, 10) == 300)
print('got:', add_funtion(290, 10) )

print("calling the add_function() with 270 and 5, expect 275 to be the result ")
print(add_funtion(270, 5) == 275)
print('got:', add_funtion(270, 5) )
```

*Hint*: Do one function at a time. And use my structure for running the functions


## User Stories
-  As a user I want to have a add_funtion() that takes in two arguments and adds them.

## Acceptance Criteria
- All core tasks done
- Separation of concerns if followed
- Dry code and functions

## Documentation

Each of the functions the calculator has to perform are coded in a different function, including addition, subtraction, multiplication and division.
All of these funcitons can take only two arguments and perform the operation between them.
```python
# Addition
def add(x, y):
    return x + y

# Subtraction
def subtract(x, y):
    return x - y

# Multiplication
def multiply(x, y):
    return x * y

# Division 
def divide(x, y):
    return x / y
```

For the more complicated functions, like calculating the areas of circles, squares and triangles, the functions require either one or two arguments.
Additionally, as the formulas are different, they had to be implemented in their own function as follows:
```python
# Find the area of a circle with the formula pi*r^2, where r is the radius
def area_of_circle(radius):
    return 3.1415*radius*radius

# Find the area of a square with the formula a*a, where a is the side
def area_of_square(side):
    return side*side

# Find the area of a triangle with the formula b*h/2, where b is the triangle base and h is the triangle height
def area_of_triangle(base, height):
    return height*base/2
```

Later, some functions are implemented that ask input from the user until the right format is recieved.

The first of these functions is used to ask the user for a choice from a number 0 to maxnum. If the user doesn't write a digit as input, or
if the number is less than 0, the program will ask for an input again.
```python
def ask_choice(max_num):
    while True:
        choice = input()
        if choice.isdigit():
            if int(choice) < max_num and int(choice) >= 0:
                return int(choice)
        print('Bad value. Try again: ')
```

Next, for the calculator, we need to ask for numbers to do the operation with. The numbers are gathered with the following function, where
the input is checked to see if it is a digit.
```python
def ask_number():
    while True:
        choice = input()
        if choice.isdigit():
            return int(choice)
        print('Bad value. Try again: ')
```

However, for the division operation, we need to check if the divisor is nonzero.
The following function is similar to the above snippet, but also checks if the inserted number is equal to 0
```python
def ask_nonzero():
    while True:
        choice = input()
        if choice.isdigit():
            if int(choice) != 0:
                return int(choice)
        print('Bad value. Try again: ')
```

Additionally, we also need to ask for a postive number when it comes to getting the are of the shapes, since the shapes can't have a negative dimension.
```python
def ask_positive_number():
    while True:
        choice = input()
        if choice.isdigit():
            if int(choice) >= 0:
                return int(choice)
        print('Bad value. Try again: ')
```

A simple function is also implemented that prints the available operations in a nicely formatted way for the user to see.
```python
def menu():
    print("Please choose an operation")
    print("""
            0. Addition
            1. Subtraction
            2. Multiplication
            3. Division
            4. Area of circle
            5. Area of square
            6. Area of triangle
            7. Exit
            """)
```

Finally, tha main program is implemented below.
The program starts with a while loop that terminates only when the user follows the exit condition.
In the while loop, the menu is printed and immediately an input is required by the user, to choose an operation with a digit (from 0 to 7)
The choice passes through a control flow of several if-else statements that checks the number value.
For each of the options, the appropriate operation is called after the right amount of numbers is requested from the users.
Also, according to the operation, a different type of number is requested, that is, for the divisor, the input has to be nonzero, etc.

```python
def calculator():
    while True:
        menu()
        choice = ask_choice(8)
        # Adddition
        if choice == 0:
            print('First number?')
            x = ask_number()
            print('Second number?')
            y = ask_number()
            print(f'Result: {add(x,y)}')
        # Subtraction
        elif choice == 1:
            print('First number?')
            x = ask_number()
            print('Second number?')
            y = ask_number()
            print(f'Result: {subtract(x,y)}')
        # Multiplication 
        elif choice == 2:
            print('First number?')
            x = ask_number()
            print('Second number?')
            y = ask_number()
            print(f'Result: {multiply(x,y)}')
        # Division 
        elif choice == 3:
            print('First number?')
            x = ask_number()
            print('Second number?')
            y = ask_nonzero()
            print(f'Result: {divide(x,y)}')
        # Area of a circle
        elif choice == 4:
            print('Radius?')
            x = ask_positive_number()
            print(f'Result: {area_of_circle(x)}')
        # Area of a square 
        elif choice == 5:
            print('Side length?')
            x = ask_positive_number()
            print(f'Result: {area_of_square(x)}')
        # Area of a triangle
        elif choice == 6:
            print('Height?')
            x = ask_positive_number()
            print('Base?')
            y = ask_positive_number()
            print(f'Result: {area_of_triangle(x,y)}')
        # Exit
        elif choice == 7:
            print('Goodbye')
            return
        else:
            print('Wrong input, try again')
 
```
