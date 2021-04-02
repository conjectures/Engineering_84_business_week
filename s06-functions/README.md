# Python: Functions

Python functions are used to encapsulate a code snippet to be used multiple times with a reference.
These functions can be used to perform many tasks, from calculating a result, to printing output or handling parsing etc.

## Creating, calling functions
Functions are created with the `def` keyword.
```python
def greetings():
    print('Welcome on board, user!')
```

They can be called with their name, followed by parenthesis (atached):
```python
greetings()
#'Welcome on board, user!'
```

## Positional Arguments 
We can create functions in python that take positional several arguments:
```python
def divide(num1, num2):
    return (num1 / num2)
```
We can pass these arguments to the funcions when calling them by adding them in the parenthesis:
```python
divide(10, 5)
# 2
```
These are called **positional arguments** as they are dependent on the position they are given to the function.
```python
divide(5, 10)
# 0.5
```






