
# Strings and Casting

# Let's have a look at some industry practices
# greetings = 'hello world'
# single_quotes = 'single quotes '
# double_quotes = "double quotes"
# 
# print(single_quotes)
# print(double_quotes)


# String Slicing
greetings = 'Hello World!'

# indexing in Python starts from 0
# H e l l o   W o r l  d  !
# 0 1 2 3 4 5 6 7 8 9 10 11

# what is the length of the string greetings?
print(len(greetings))
# The len() method is used to find the length of the statement

print(greetings[0:5])
print(greetings[6:11])

# Reverse indexign starts from -1
print(greetings[-6:])


# Let's have a look at some string methods
white_space = 'Lots of space after this text,           and some space at the end            '
# strip() helps us remove white spaces
print(len(white_space))
print(len(white_space.strip()))
print((white_space.strip()))

# count the number of times a pattern is in a string:
print(white_space.count('space'))

# Change the text into uppercase
print(white_space.upper())
print(white_space.lower())
print(white_space.capitalize())
print(white_space.replace("space", "blankspace"))


# Concatenation and Casting
first_name = "James"
last_name = "Bond"
age = 30
print(first_name + " " + last_name)
print(first_name, last_name, age)


# F strings
#easier formatting
print(f'{first_name} {last_name} is {age} years old')
print(f"{first_name=}") # python 3.8


