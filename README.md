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

