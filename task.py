# Task 1

try:
    file = open('orders.txt', 'r')
    print('File found')
    data = file.read()
    for line in data:
        print(line)

except IOError:
    print('The above block was not executed')
finally:
    print("Thank you")
