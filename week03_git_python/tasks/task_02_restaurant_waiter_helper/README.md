# TASK 2 - Restaurant Waiter Helper Program

## Summary
Now that we've created had some time to use our lists, time to make something more useful.
You are going to make a program that helps a waiter with his menu and his orders.
See tasks for the user stories.

## User stories
1.  AS a User I want to be able to see the menu in a formated way, so that I can order my meal.
2.  AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten
3.  As a user, I want to have my order read back to me in formated way so I know what I ordered.

## Acceptance Criteria
- its own project on your laptop and Github
- be git tracked
- have 5 commits mininum!
- has documentation
- follows best practices

## Documentation
Run the program with `python main.py`, or `python3` according to python version. 
**The program uses python 3.7++**

The menu will immediately appear and user input will be required:
```
Please choose an item:
	0. burger, (main  $14)
	1. fires, (side  $3)
	2. cheeseburger, (main  $16)
	3. soda, (drink  $2)
Choose item 1:
```
The number of the choice is also shown when as user input is requested, ie. `Choose item >1<`

Only 3 items can be chosen in the current iteration of the program, no more, no less. (choices cannot be skipped)

In the end, the full order will be printed, along with the total cost:
```
Here is what you ordered:
  Item 0: fries for $3
  Item 1: cheeseburger for $16
  Item 2: soda for $2
Total: 21
```

## Solution
A sample menu was created and added as a list in global scope that contains dictionary entries for each item:
```python
menu_list = [
        {'item': 'burger', 'category': 'main', 'price': 14},
        {'item': 'fires', 'category': 'side', 'price': 3},
        {'item': 'cheeseburger', 'category': 'main', 'price': 16},
        {'item': 'soda', 'category': 'drink', 'price': 2},
        ]
 ```

A function was written that handles the printing of the menu in a pretty format. 
This function iterates through the menu list and prints each item name, category and price
```python
def menu():
    print('Please choose an item:')
    for idx, item in enumerate(menu_list):
        print(f"\t{idx}. {item.get('item')}, ({item.get('category')}  ${item.get('price')})")
```

A different function is used to handle the user input.
The user will be required to enter numbers between 0 and the length of the list to choose items. 
Therefore the function has a while loop and keeps asking for user to provide a digit if it is not, and for the digit to be within specified range:
```python
def ask_number(max_num):
    while True:
        choice = input()
        if choice.isdigit():
            if int(choice) < max_num and int(choice) >= 0:
                return int(choice)
        print('Bad value. Try again: ')
```

Finally in the main function, the required variables are initialized, that is, the choices list, the total amount var and the number of choices the user has.
The menu is called after that and the user input is requested for the amount of times specified. 

```python
def main():

    # list to store choices
    choices = []
    # var to store the total cost of order (initialise to zero)
    total = 0
    # only 3 choices allowed
    num_choices = 3

    # ask for customer choices
    for i in range(num_choices):
        menu()
        print(f'choose item {i+1}:  ')
        # append choice to list
        choices.append(ask_number(len(menu_list)))
        # add price to total
        total += menu_list[choices[-1]].get('price')

    # print order
    print(f'here is what you ordered:')
    for idx, choice in enumerate(choices):
        print(f"  item {idx}: {menu_list[choice].get('item')} for ${menu_list[choice].get('price')}")
    print('total: {}'.format(total))

```
In the end, the full order is printed by iterating throught the choices list, and using the user input to find the appropriate dictionary entry.

