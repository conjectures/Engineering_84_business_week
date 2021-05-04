# Task 1
# Read data and display it as a list

try:
    items = []
    file = open('orders.txt', 'r')
    print('File found')
    for line in file:
        items.append(line.rstrip('\n'))
    print(items)
except IOError:
    print('The above block was not executed')
finally:
    print("Thank you")
