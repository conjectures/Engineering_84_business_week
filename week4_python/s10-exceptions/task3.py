# Task 3
# Function to append item to file
# 'a' - Open file in append mode. If file does not exist, it creates a new file

def append_to_file(filename, item):
    try:
        items = []
        file = open(filename, 'a')
        file.write(item)
    except IOError:
        print('The above block was not executed')
    finally:
        print("Thank you")

if __name__ == '__main__':
    print("Adding item 'icecream'")
    item = 'icecream'
    filename = 'orders.txt'
    append_to_file(filename, item)
