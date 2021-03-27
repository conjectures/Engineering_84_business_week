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


# PART 2
# prompt the user for input and re-assing the variable age and name
# figure out a way to account for if the persons bithday has already happened this year or not

name = input('What is your name?\n')
reprompt = True
while reprompt:
    age = input('When were you born? (year)\n')
    # Check if input is a number
    if age.isdigit():
        reprompt = False
    else:
        print('Bad value. Try again.')

bday = input('Did you have your birthday this year? (y/n)\n').lower()
while bday not in ['n', 'no', 'y', 'yes']:
    bday = input("Sorry, i didn't catch that, did you already have your birthday this year? (y/n)\n").lower()

# If birthday passed, add a year to their age
if bday in ['n', 'no']:
    year_born = current_year - age - 1
else:
    year_born = current_year - age

print(f'OMG {name}, you are {age} years old, so you were born in {year_born}\n\n')
