# pseudocoding

# Testing env with hello world message
print("Hello, world")

# What is a variable?
course_name = 'devops 84'  # string
student_name = 'alex'  # another string
age = 16  # int
hourly_wage = 8.9  # float

print(student_name)
print(age)  # python will 'translate' the age integer into string when printing
print(hourly_wage)  # same as float

# We can use `input()` to get data from user:
first_name = input('What is your name?')

print(f'hello {first_name}')

age = input('What is your age?')
# Check data type of variable with type()
print(type(age))

# Change the datatype to int with int()
print(type(int(age)))
