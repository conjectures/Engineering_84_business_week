# TASK 1  - Calculate the year of birth of a user

## Tasks:
Part 1:
- Define the variables `age` and `name`
- Make a calculation for the year in which the person was born.
- Print out "OMG [person], you are [age] years old so you were born in [year]" with the correct values.

Part 2:
- Prompt the user to input values for the variables `age` and `name`
- Check the user's input to make sure it is correct (age must be a number)
- Figure out a way to account for if the user's birthday has already happened this year or not

Extra:
- Look into the library `time`
- Print out how long this person has lived in hours

## Solutions

Initially, the datetime library is imported and is used to find the current year.
```python 
import datetime

current_time = datetime.datetime.now()
current_year = current_time.year
```

Later the details of a person were defined so that they can be later be used in the f-string and calculation.
```python
age = 20
name = 'bob'

print(f'OMG {name}, you are {age} years old, so you were born in {current_year-age}\n\n')
```

In the second part of the task, the variables `age` and `name` are overwritten with input from the user.
For this reason, the user program had to reject unsuitable values and request a new one immediately after:
```python
name = input('What is your name?\n')
reprompt = True
while reprompt:
    age = input('When were you born? (year)\n')
    # Check if input is a number
    if age.isdigit():
        reprompt = False
    else:
        print('Bad value. Try again.')
```
Later, the user is asked whether his birthday has passed this year. This will be used in order to calculate the year of his
birth.
```python
bday = input('Did you have your birthday this year? (y/n)\n').lower()
while bday not in ['n', 'no', 'y', 'yes']:
    bday = input("Sorry, i didn't catch that, did you already have your birthday this year? (y/n)\n").lower()

```
Finally, we subtract a year if his birthday hasn't passed yet.
> To showcase why that is, let's suppose a person is born in the year 2000. By 2020 he will be 20 if his birthday came up, or 19 if it hasn't.
> On the other hand, for the same person, if the year is 2020 and we know he is 20 years old and his birthday came up this year, he will probably have been born in the year 2000. 
> However, if it hasn't, then he should turn 21 soon which means he was born in 1999.
```python
# If birthday passed, add a year to their age
if bday in ['n', 'no']:
    year_born = current_year - age - 1
else:
    year_born = current_year - age

print(f'OMG {name}, you are {age} years old, so you were born in {year_born}\n\n')
```

