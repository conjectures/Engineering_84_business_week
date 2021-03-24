# Python: Control FLow
> Eng84 week 3 day 2 & 3

Conditional statements are used to control the flow of our program

### If, elif and else

The most common way to create a control flow in python is with the keywords `if`, `elif`, `else`

Example:

```python
# Check for conditionA
if age > 15:
  # Prints if conditionA == True
  print('Please proceed with purchase')
# Check conditionB
elif age == 15:
  # Prints if conditionA == False, AND conditionB == True
  print('Please provide one more form of identification')
else:
  # Prints if conditionA == False AND conditionB == False
  print('Sorry, you are not allowed to buy')
```


## Loops
Loops help us iterate through the data, or repeat a piece of code for a number of times

### For loop

For example, if we want to view the items of a shopping list:
```python
shopping_list = ["bread", "eggs", "milk", "orange"]

# Print each item
print(shopping_list[0])
print(shopping_list[1])
print(shopping_list[2])
print(shopping_list[3])
```
Instead, of printing each item index, we can iterate over the item with a for loop:
```python
for items in shopping_list:
    print(items)
```
With the above code snippet, we have transformed our code into a simpler and more readible form.

To iterate through dictionaries, we first need to 'transform' them into iterables with the `items()`, `values()` or `keys()` methods, according to use case:

```python
bill = {
        'table1': {'patron': 'James', 'bill': 25},
        'table2': {'patron': 'John', 'bill': 51.2},
        'table3': {'patron': 'Jim', 'bill': 32.6},
        }

for value in bill.values():
    print(f"{value.get('patron')} with a bill of {value.get('bill')}")
```

### While loop
While loops are loops that repeat as long as a condition is being met.
They are commonly used to interact with user, and request input until it is given in the right format. Other use cases include
menus, or even games, when frames need to be redrawn as long as the game is active.

While loops can work in the same way as for loops, if needed:
```python
num = 0
while num < 10:
    print(f"Number is: {num}")
    num += 1
```
We can also break from the while loop, just as in the for loop:
```python
num = 0
while num < 10:
    print(f"Number is: {num}")
    # Stop looping if number is 4
    if num == 4: 
      break;
    num += 1
```
Usually, the while loop is used as a menu, to ask for user input:
```python
user_prompt = True
while user_prompt:
    age = input("Please enter your age: ")
    if age.isdigit():
        user_prompt = False
    else:
        print("Please enter your age in digits.")
```
