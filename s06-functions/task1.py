
# Task 1
# Create a calculator to add, subtract, divide, multiply
# Display appropriate messages with result

def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    return x/y


def menu():
    print("What would you like to do?")
    print("""
            \n1) add
            \r2) subtract
            \r3) multiply
            \r4) divide
            \r5) quit
            """)
    return input()


def get_number(text):
    num = ''
    while not num.isdigit():
        print(text)
        num = input()
    return int(num)


def calculator():
    choice = menu()
    while (not choice.isdigit()) and (choice not in ['1', '2', '3', '4']):
        choice = menu()

    choice = int(choice)
    if choice == 5:
        return
    # Get numbers
    numA = get_number('Please input a number')
    numB = get_number('Please input another number')

    if choice == 1:
        print(f'The result is {numA + numB}')
    elif choice == 2:
        print(f'The result is {numA - numB}')
    elif choice == 3:
        print(f'The result is {numA * numB}')
    elif choice == 4:
        print(f'The result is {numA / numB}')
    else:
        return


if __name__ == '__main__':
    calculator()
