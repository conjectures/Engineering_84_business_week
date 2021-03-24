# TASK 4 - Fizz Buzz!
# Super simple game that will substitute multiples of 3 and 5 for fizz an buzz respectily, or fizzbuzz for multiples of the two


# Function that completes the fizzbuzz challenge for arbitrary numbers
def fizzbuzz(numA, numB, maxnum):
    # create number list
    numbers = list(range(1, maxnum))
    # iterate through the numbers
    for i in numbers:
        # Check if number is modulo of number A or number B, and create an appropriate string
        temp = ('Fizz' if not i % numA else '') + ('Buzz' if not i % numB else '')
        if temp is not '':
            # Assign string to list with index i-1 (lists index from 0 while the numbers start from 1)
            numbers[i-1] = temp
    return numbers


# Function that asks for user input until digit is passed
def ask_number(max_num):
    while True:
        choice = input()
        if choice.isdigit():
            if int(choice) < max_num and int(choice) >= 0:
                return int(choice)
        print('Bad value. Try again: ')


# print(fizzbuzz(3, 5, 100))
max_num = 100
print('Fizz at?')
numA = ask_number(max_num)
print('Buzz at?')
numB = ask_number(max_num)
print('Here is your fizzbuzz!')
print(fizzbuzz(numA, numB, max_num))
