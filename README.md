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

# Change item at index 0
shopping_list[0] = 'orange'
# ['orange', 'chocolate', 'avocados', 'milk']

# Append item
shopping_list.append('cherries')
# ['orange', 'chocolate', 'avocados', 'milk', 'cherries']

# Remove from list
shopping_list.remove('orange')
# ['chocolate', 'avocados', 'milk', 'cherries']

# Insert item in list at index 0
shopping_list.insert(0, 'linguini')
# ['linguini', 'chocolate', 'avocados', 'milk', 'cherries']

# Pop item - remove item at index
popped_item = shopping_list.pop(1)
# popped_item = 'chocolate'
# shopping_list = ['linguini', 'avocados', 'milk', 'cherries']

```
