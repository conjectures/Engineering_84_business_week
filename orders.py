# Dealing with files  and error/ exceptions

# There is a built in method in python called `open`
# file = open('orders.txt') # looks for file called 'orders.txt'

try:
    # file = open('orders01.txt')
    file = open('orders.txt')
    print('File found')
except IOError:
    print('The above block was not executed')
finally:
    print("Thank you")

# task 1: read data and display it as a list
# task 2: function to do the same job
