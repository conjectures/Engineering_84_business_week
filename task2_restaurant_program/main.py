
# Store items in a list with dictionary entries
menu_list = [
        {'item': 'burger', 'category': 'main', 'price': 14},
        {'item': 'fires', 'category': 'side', 'price': 3},
        {'item': 'cheeseburger', 'category': 'main', 'price': 16},
        {'item': 'soda', 'category': 'drink', 'price': 2},
        ]


# Function that displays the menu in a pretty format
def menu():
    print('Please choose an item:')
    for idx, item in enumerate(menu_list):
        print(f"\t{idx}. {item.get('item')}, ({item.get('category')}  ${item.get('price')})")


# Function that asks for input that is a digit and within a range
def ask_number(max_num):
    while True:
        choice = input()
        if choice.isdigit():
            if int(choice) < max_num and int(choice) >= 0:
                return int(choice)
        print('Bad value. Try again: ')


# Function that acts as main program
def main():

    # list to store choices
    choices = []
    # var to store the total cost of order (initialise to zero)
    total = 0
    # Only 3 choices allowed
    num_choices = 3

    # Ask for customer choices
    for i in range(num_choices):
        menu()
        print(f'Choose item {i+1}:  ')
        # Append choice to list
        choices.append(ask_number(len(menu_list)))
        # Add price to total
        total += menu_list[choices[-1]].get('price')

    # Print order
    print(f'Here is what you ordered:')
    for idx, choice in enumerate(choices):
        print(f"  Item {idx}: {menu_list[choice].get('item')} for ${menu_list[choice].get('price')}")
    print('Total: {}'.format(total))


if __name__ == '__main__':
    main()
