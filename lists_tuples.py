
# What is a list
# simple storage of data, they are mutable, syntax with []

shopping_list = ["bread", "chocolate", "avocados", "milk"]

print('List type')
print(type(shopping_list))
print('\nIndexing in lists')
print(shopping_list[1])
print(shopping_list[-2])

# Change the value of 0 index to "orange"
print(shopping_list)
print('\nChange item')
shopping_list[0] = 'orange'
print(shopping_list)

print('\nAppend item')
shopping_list.append('cherries')
print(shopping_list)
print('\nRemove item from list')
shopping_list.remove('orange')
print(shopping_list)

print('\nInsert item in list at index 0')
shopping_list.insert(0, 'linguini')
print(shopping_list)
