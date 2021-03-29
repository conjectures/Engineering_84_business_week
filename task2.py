# Task 2
# Function to do the same job

def read_and_print(filename):
    try:
        items = []
        file = open(filename, 'r')
        print('File found')
        for line in file:
            items.append(line.rstrip('\n'))
        print(items)
    except IOError:
        print('The above block was not executed')
    finally:
        print("Thank you")
