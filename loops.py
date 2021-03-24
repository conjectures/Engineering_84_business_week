
# Loops syntax
# Use for keyword before a data collection

shopping_list = ["bread", "eggs", "milk", "orange"]
print(shopping_list)

# for example, let's iterate through the shopping list.
for items in shopping_list:
    print(items)

# Strings are also iterable:
for letter in "fruits":
    print(letter)

# We can combine if statements with loops
for items in shopping_list:
    print(items)
    # If the condition below is True, the loop will stop (break)
    if items == 'milk':
        break


print()
print()

# Including to lists and strings, we can iterate over a dictionary:
bill = {
        'table1': {'patron': 'James', 'bill': 25},
        'table2': {'patron': 'John', 'bill': 51.2},
        'table3': {'patron': 'Jim', 'bill': 32.6},
        }

for value in bill.values():
    print(f"{value.get('patron')} with a bill of {value.get('bill')}")
