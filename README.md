# Exception Handling in Python 

Dealing with files and Exception Handling with Python

We have `try` `except`, `raise` and `finally` as our code blocks handle the error or an exception.

To understand this concept easily:
Each block of code works as an if, elif, else block

We create a file called `orders.txt` and try to read it with the `orders.py` file:
```
# In orders.txt
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

