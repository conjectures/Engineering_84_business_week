# TASK 5 - CALCULATOR
# Author: Alexis

# **_Core:_**
# 1. Build a function containing:
#   - Add
#   - Subtract
#   - Multiply
#   - Divide

# 2. Buld more functions for 
#   - Area of a circle
#   - Area of a square
#   - Area of a triangle

# **_Extra:_**
# - Run function with arguments
# - Assert against known values. Adding 10+30 will alwyas be 40


#Define functions for calculations
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def area_of_circle(radius):
    return 3.1415*radius*radius


def area_of_square(side):
    return side*side


def area_of_triangle(base, height):
    return height*base/2


def ask_choice(max_num):
    while True:
        choice = input()
        if choice.isdigit():
            if int(choice) < max_num and int(choice) >= 0:
                return int(choice)
        print('Bad value. Try again: ')


def ask_number():
    while True:
        choice = input()
        if choice.isdigit():
            return int(choice)
        print('Bad value. Try again: ')


def ask_positive_number():
    while True:
        choice = input()
        if choice.isdigit():
            if int(choice) >= 0:
                return int(choice)
        print('Bad value. Try again: ')


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


def calculator():
    while True:
        menu()
        choice = ask_choice(8)
        if choice == 0:
            print('First number?')
            x = ask_number()
            print('Second number?')
            y = ask_number()
            print(f'Result: {add(x,y)}')
        elif choice == 1:
            print('First number?')
            x = ask_number()
            print('Second number?')
            y = ask_number()
            print(f'Result: {subtract(x,y)}')
        elif choice == 2:
            print('First number?')
            x = ask_number()
            print('Second number?')
            y = ask_number()
            print(f'Result: {multiply(x,y)}')
        elif choice == 3:
            print('First number?')
            x = ask_number()
            print('Second number?')
            y = ask_number()
            print(f'Result: {divide(x,y)}')
        elif choice == 4:
            print('Radius?')
            x = ask_positive_number()
            print(f'Result: {area_of_circle(x)}')
        elif choice == 5:
            print('Side length?')
            x = ask_positive_number()
            print(f'Result: {area_of_square(x)}')
        elif choice == 6:
            print('Height?')
            x = ask_positive_number()
            print('Base?')
            y = ask_positive_number()
            print(f'Result: {area_of_triangle(x,y)}')
        elif choice == 7:
            print('Goodbye')
            return
        else:
            print('Wrong input, try again')
        print('\n')


if __name__ == '__main__':
    calculator()
