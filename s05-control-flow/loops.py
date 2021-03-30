
# Loops syntax
# Use for keyword before a data collection
print("For Loops")
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



# While Loop

# Use case 1 - 'simulate' for loop
print("\n\nWhile Loops:")
num = 0
while num < 10:
    print(f"print number -> {num}")
    num += 1

# We can also stop the loop with the break keyword
print("\nUsing break")
num = 0
while num < 10:
    print(f"print number -> {num}")
    if num == 4:
        break
    num += 1

# Use case 2 - ask user input
print("\nAsking user for input")
user_prompt = True
while user_prompt:
    age = input("Please enter your age: ")
    if age.isdigit():
        user_prompt = False
    else:
        print("Please enter your age in digits.")

print(f"Your age is {age}.")  # only gets executed if user enters age in digits
