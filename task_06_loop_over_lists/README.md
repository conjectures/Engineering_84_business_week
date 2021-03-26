# TASK 6 - Loops Over Lists

## Summary
Let's loop over some lists!

## Tasks
1. Make a loop with a range that says hello 10 times
2. Create another loop with a range that asks for names and appends to list_names
3. Make a loop that iterated over each name in lit_name and format's it into lowercase in a new variable called list_names_lower
4. Iterate over the list of values to find if the are even

## Acceptance Criteria
- All tasks done

## Documentation

1. In the first task, a simple list is created with the keyword `range()`. This list is an iterable with 10 'values' from 0 to 9.
We iterate through this list and print hello for each item.
```python
for i in range(10):
    print(f'{i}. Hello')
```

2. For the second task, we have to create an infinite loop that takes in the inputs from the user and appends them in a list.
Firstly, the list is initiated, then a `while` loop starts.
In the while loop, the program requests user input and checks if it is equal to 'exit', as a condition to break the loop.
Later the name is appended, with the keyword `append`. When the loop stops, the full list is displayed
```python
print("\n\nList of names")
list_name = []
while True:
    name_input = input("Write a name, write 'exit' to leave:  " )
    if name_input.lower() == 'exit':
        break
    list_name.append(name_input)
print(list_name)
```
3. In this task, we iterate through the list that was created previously and transfrom them to lowercase.
To achieve this, a list comprehension is used where the `lower()` string method is applied to each item in the list.
The list comprehension produces a list that includes only the lower case forms of the names. This list is displayed after the program ends.
```python
print("\n\nLower case list with names")
# Make a loop that iterated over each name in lit_name and format's it into lowercase in a new variable called list_names_lower
list_name_lower = [name.lower() for name in list_name]
print(list_name_lower)
```

4. Finally, in the fourth task, we iterate over a range of numbers and print wether they are even or odd. 
Firstly, the program asks for a positive number from the user. Then, the number is used to generate a list from a range of numbers.
After that, a list comprehension is used to traverse a range of numbers, and applies a modulo operation to each index. 
If the modulo operation reults to zero, the string 'even' is returned, else it gets the string 'odd'. Finally, the list that is generated
from the comprehension is printed below.

# Iterate over the list of values to find if the are even
```python
print("\n\nEven Odd list")
prompt = True 
while prompt:
    temp = input('Please input a positive number:   ')
    if temp.isdigit():
        if int(temp) >= 0:
            prompt = False

even_odd_list = [f'{i} is even' if i%2 else f'{i} is odd' for i in range(int(temp))]
for item in even_odd_list:
    print(item)
```
