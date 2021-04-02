
# What is a function?
# Why do we use it
# How to create a function


# Syntax: keyword `def` is used to declare the start of a function

# Let's create a function named 'greetings'
def greetings():
    print('Welcome on board, user!')


# By running this file with python, the function will not execute, unless explicitly called.
print("This will execute before the function")

# And now we call the function
greetings()


# Define a new function that takes parameters
def greet_user(user):  # user is a `positional` argument
    print(f"Welcome on board, {user}")


# If the function is defined with positional parameters, it will give an error if the parameter is not passed
try:
    # This will cause an error
    greet_user()
except TypeError:
    print("TypeError ...")

# If we pass a parameter to the function, it will execute correctly
try:
    greet_user("alex")
except TypeError:
    print("TypeError ...")


print("\n Create a function that prints the result of addition of 2 arguments")


def add(num1, num2):
    print(num1 + num2)


# No need to return the value as its being printed. However it is less flexible as we don't get to use the value
add(3, 2)

print("\n Use return statement for the same function (instead of printing)")


def add(num1, num2):
    return num1 + num2


# Calling the function will return the result, letting us use it in more profound ways
print(add(3+2))

print('\nStatements after a return command will not get a chance to be executed')


def subtract(num1, num2):
    return num1 - num2
    print("The result will be negative if num1 < num2 ")


subtract(2, 3)

#
