# Exception Handling in Python 

Dealing with files and Exception Handling with Python

We have `try` `except`, `raise` and `finally` as our code blocks handle the error or an exception.

To understand this concept easily:
Each block of code works as an if, elif, else block

We create a file called `orders.txt` and try to read it with the `orders.py` file:
```txt
# In orders.txt
// orders.txt file
pizza
salad
soda
```

```python
# In orders.py
try:
    # file = open('orders01.txt')
    file = open('orders.txt')
    print('File found')
except IOError:
    print('The above block was not executed')
finally:
    print("Thank you")
```
The above code will execute correctly even if the `orders.txt` file does not exist.
We can try this by changing the filename to be opered to `orders01.txt` was not created yet.
The except block will catch the error and print a message, instead of stopping execution.

## Note: IO with files using Python

| Mode |Description|
| :----: |:---- |
|'r' |This is the default mode. It Opens file for reading. |
|'w' |This Mode Opens file for writing. If file does not exist, it creates a new file. If file exists it truncates the file.|
|'x' |Creates a new file. If file already exists, the operation fails.|
|'a' |Open file in append mode. If file does not exist, it creates a new file.|
|'t' |This is the default mode. It opens in text mode.|
|'b' |This opens in binary mode.
|'+' |This will open a file for reading and writing (updating)|


It is worth noting that the `+` operator can be used with

## CRUD
Stands for `create`, `read`, `update`, `delete`.
