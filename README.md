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


