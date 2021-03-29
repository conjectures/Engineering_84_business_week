# Python: Data Collections

- Lists and Tuples
- Dictionary
- Sets


### What are lists?
They are commonly used to store data
Lists are mutable (can be changed)
They are created with square brackets '[]'
Indexing for lists also starts from 0

```python
shopping_list = ["bread", "chocolate", "avocados", "milk"]
```

- We can change any item in the list by indexing it and then assigning a value
```python
# Change item at index 0
shopping_list[0] = 'orange'
# ['orange', 'chocolate', 'avocados', 'milk']
```

- We can append an item to a list with the `append()` method
```python
# Append item
shopping_list.append('cherries')
# ['orange', 'chocolate', 'avocados', 'milk', 'cherries']
```

- Additionally, an item can be inserted into an arbitrary index with the `insert()` method. 
```python
# Insert item in list at index 0
shopping_list.insert(0, 'linguini')
# ['linguini', 'chocolate', 'avocados', 'milk', 'cherries']
```

- An item can be removed from the list, if we now its value
```python
# Remove from list
shopping_list.remove('orange')
# ['chocolate', 'avocados', 'milk', 'cherries']
```

- Additionally, items can be removed via their index (if we don't know or need to provide the value)
```python
# Pop item - remove item at index
popped_item = shopping_list.pop(1)
# popped_item = 'chocolate'
# shopping_list = ['linguini', 'avocados', 'milk', 'cherries']
```

<br>

## What are tuples?
Tuples are exactly the same as lists, but they are IMMUTABLE. 
They use the round brackets for syntax, i.e `()`

When we try to change a value inside a tuple, we get a `TypeError`:
```python
TypeError: 'tuple' object does not support item assignement
```

## What are dictionaries?
Dictionaries use KEY VALUE pairs to save the data.
The data can be retrieved by its value, or by its key.
They are mutable and they are created inside the curly brackets, i.e. `{}`

Additionally, dictionaries can also contain lists.
```python
dev= {
        "key": "value",
        "name": "James",
        "stream": "DevOps",
        "completed": 3,
        "completed_names": ['Variables', 'Data Types', 'Collections']

        }
```
- Getting values
- Addinng key-values
- Removing
- Updating values

## What are Sets?
Sets also use curly brackets `{}`
They are unordered. The position of the items is not guaranteed (and unpredictable)
```python
car_parts = {"wheels", "engine", "doors"}
```

- Adding to sets:
```python
car_parts.add('seats')
```

- Removing from sets:
```python
car_parts.discard('engine')
```
