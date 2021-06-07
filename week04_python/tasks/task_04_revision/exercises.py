import copy

# Create a function called 'greetings' that takes one argument as string and returns it with a 'hello'

def greetings(name):
    return f'Hello, {name}'

# Declare a list of numbers from 1 to 9, iterate through and print the list
listA = list(range(1,10))

for x in listA:
    print(x)

# EXC 3
# Write boolean operators
# If a == b and c == d print True

if 'a' == 'b' and 'c' == 'd':
    print('True')

print("\n\nTask5")
# EXC 5
# Create a list of 5 numbers, starting from 0
listB = list(range(5))
# Create a tuple with same info
tupleB = tuple(listB)
# Change value of tuple in the last index
# Answer: Tuples are immutable, they cannot be changed
listC = copy.deepcopy(listB)
listC[-1] = 100
tupleC = tuple(listC)
print(listB)
print(tupleB)
print(tupleC)

# EXC 6
# Create a dictionary with 2 key pairs
# 1st key: 'name' with value 'james'
# 2nd key: 'age' with integer value 18
# display the value and keys
dictA = {
        'name': 'james',
        'age': 18
        }

print(dictA.get('name'))
print(dictA.get('age'))

# Create a class called isobel and initialise the class that takes two arguments
# Create an object of that class
class Isobel:
    def __init__(self, *args):
        self.args = args
        pass
    
    def __repr__(self):
        return f"Hey, I'm isobel"

isobel = Isobel(1,2)
print(isobel)

# Create another object from the same class called student and print the attributes
student = Isobel(10,20)
print(student.args)


# TASK 7
# Write the correct syntax to create a set
setA = {1, 2, 3, 4}
# Write difference between sets and all other collections
# ANSWER: unordered
print("\n\n\n")
print(setA)
# Add number to set
setA.update({5})
print(setA)
setA.add(10)
print(setA)

# TASK 8
# Create a method that takes one argument as a string(my name)
# if name equals to 'dunni', return true, else false
print("\n\n\n")
def is_dunni(name):
    if name == "Dunni":
        return True
    return False

print(is_dunni("Dunni"))


# TASK 9
# Create a class called human with one method called breathe that returns breathing
# Create another class called student that inherits from human and create an object of student class.
# Finally, call the method from the parent class
print("\n\n\n\nTASK 9")
class Human:
    def __init__(self):
        self.alive = True

    def breathe(self):
        return 'breathing'

class Student(Human):
   "Student class" 

me = Student()
print(me.breathe())



# TASK 10
# Write the correct syntax to use the synctax super
print("\n\nTASK 10")
class HumanA:
    def __init__(self):
        self.alive = True

    def breathe(self):
        return 'breathing'

# super refers tot the parent class. WHen used in this manner, we can use methods of the parent class to affect the child
class StudentA(Human):
    def __init__(self):
        super().__init__()

student = StudentA()
print(student.alive)
# TASK 11
print("\n\nTASK 11")
# Create a function that takes an argument as a list
# Create a varuable called user_data and store 0 to 4 in that list
# THe function returns True if the datatype is a list, False otherwise
user_data = list(range(5))

def is_list(data):
    return isinstance(data, list)

print(user_data)
print(is_list(user_data))

# TASK 12
print("\n\n\nTASK 12")
# Create a function called 'get_percentage', takes two integers as arguments, returns percentage of the two
def get_percentage(num1, num2):
    percentage = num1 / (num1 + num2) * 100
    return percentage

print(get_percentage(10,90))


# TASK 13
print("\n\n\nTASK 13")
# Create or declare a function that takes two args as integers and divide the first value by the second value. Return the outcome
# Check if the number given is divisible by zero. If that is the case, send a message it can't be divided by 0 and the value
def divide(numA, numB):
    if not numB:
        print(f"{numA} is not divisible by 0")
        return
    else:
        return numA / numB


## TASK 14
print("\n\n\nTASK 14")
# Write five odd numbers in a list and then five even numbers in another list.
# Iterate through these lists to combine and display the numbers in a method
odd_numbers = [1, 3, 5, 7, 9]
even_numbers = [2, 4, 6, 8, 10]

combined = [] 

for x, y in zip(odd_numbers, even_numbers):
    combined.append(x)
    combined.append(y)

print(combined)


# TASK 15
print("\n\n\nTASK 15")
# create a dictionary called shoppint_list with 3 key value pairs
# milk 1gbp, yogurt 1.15gbp, ice cream 2.38
# create a function that takes an arg as the dictionary and iterate trhough the values of the dictionary. Add the total value and return the cost


shopping_list = {
        'milk': 1,
        'youghurt': 1.15,
        'ice-cream': 2.30
        }

def add_shopping(data):
    return sum(data.values())

print(add_shopping(shopping_list))


## TASK 16
print("\n\n\nTASK 16")
## 
