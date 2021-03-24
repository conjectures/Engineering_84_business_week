# Python: Control FLow

Conditional statements are used to control the flow of our program

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

- for
- while

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




