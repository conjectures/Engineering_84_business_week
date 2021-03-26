# TASK 9 - Control Flow Age and Permission

# # Inputs
# age = 19
# driver_lisence = True
#
# # Outputs
# - You can vote and drive
# - You can vote
# - You can driver
# - you can't legally drink but your mates/uncles might have your back (bigger 16)
# - Your too young, go back to school!

def get_permission(age, driver_license):
    # Check if age is number
    if isinstance(age, str):
        if age.isdigit():
            age = int(age)
        else:
            print('Bad value')
            return
    # age <= 16
    #   no drinking
    #   no voting
    #   no driving
    if age <= 16:
        print('You are too young, go back to school')

    # 16> age < 17
    #   maybe drinking
    #   no voting
    #   no driving
    elif age < 17:
        print('You might drink a little although illegal')
    # 17 >= age < 18
    #   maybe drinkin
    #   no voting
    #   driving if license == True
    elif age < 18:
        if driver_license:
            print('You can drive')
        else:
            print("You still can't drive")
    # age > 18
    #   drinking
    #   voting
    #   driving if license == True
    else:
        if driver_license:
            print('You can vote and drive')
        else:
            print('You can drive')


# Function used to get a number from user input, ask again if not appropriate and return it as integer
def ask_number():
    while True:
        choice = input()
        if choice.isdigit():
            choice = int(choice)
            if num_in_bounds(choice):
                return choice
        print('Bad value. Try again: ')


# Check if the number is above 0
def num_in_bounds(number):
    if number > 0:
        return True
    return False


# Return True if value is 'y' or 'yes'. Return False if 'n' or 'no'. Return None otherwise
def yes_no_true_false(value):
    if value.lower() in ['y', 'yes']:
        return True
    elif value.lower() in ['n', 'no']:
        return False
    return None


# Continue asking for user input until yes or no is given
def ask_yes_no():
    while True:
        choice = yes_no_true_false(input())
        if choice is not None:
            return choice
        print('Bad value')


def showcase():
    print("If i am 12 years old and i have a fake drivers license")
    get_permission(12, True)

    print('\nIf i am 16 and a half, again with fake license')
    get_permission(16.5, True)

    print('\nIf i am 17 and a half without a license')
    get_permission(17.5, False)

    print('\nIf i am 17 and a half and finally got my license')
    get_permission(17.5, True)

    print('\nWhen i turn 18')
    get_permission(18, True)

    print('\nIf lose my license at 55')
    get_permission(55, False)


def main():
    while True:
        choice = input("\nCheck your permissions?\n (Enter any value to continue, or enter 'exit' to quit)\n")
        if choice.lower() == 'exit':
            break
        print('What is your age?')
        age = ask_number()
        if age >= 17:
            print('Do you have a license(y/n)?')
            drivers_license = ask_yes_no()
            get_permission(age, drivers_license)
        else:
            # if driver is less than 17 don't even ask for license
            get_permission(age, False)
    print('Goodbye')


if __name__ == '__main__':
    main()

