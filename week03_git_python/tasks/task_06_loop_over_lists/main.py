# TASK 6 - LOOP OVER LISTS
# Author: Alexis 

# Make a loop with a range that says hello 10 times
print("\n\nHello from list")
for i in range(10):
    print(f'{i}. Hello')


# Create another loop with a range that asks for names and appends to list_names
print("\n\nList of names")
list_name = []
while True:
    name_input = input("Write a name, write 'exit' to leave:  " )
    if name_input.lower() == 'exit':
        break
    list_name.append(name_input)
print(list_name)


print("\n\nLower case list with names")
# Make a loop that iterated over each name in lit_name and format's it into lowercase in a new variable called list_names_lower
list_name_lower = [name.lower() for name in list_name]
print(list_name_lower)


# Iterate over the list of values to find if the are even
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

