import datetime

# PART 1
# define the variables age and name
# make a calculation for the year in which the person was born
# print out "OMG <person>, you are <age> years old so you were born in <year>" with the correct values

current_time = datetime.datetime.now()
current_year = current_time.year


age = 20
name = 'bob'

print(f'OMG {name}, you are {age} years old, so you were born in {current_year-age}\n\n')

#PART 2
# prompt the user for input and re-assing the variable age and name
# figure out a way to account for if the persons bithday has already happened this year or not

name = input('What is your name?')
reprompt = True
while reprompt:
    age = input('What is your age?')
    if age.isdigit():
        reprompt = False
    else:
        print('Please enter a correct value')

# TODO


