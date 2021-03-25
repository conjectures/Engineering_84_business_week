
# Let's create our first class
# syntax: `class` is the key word

class Animal():

    # Can name attributes here
    name = "Dog"    # class variable

    # The init method refers to the initialization functionality of the class
    def __init__(self):  # self refers to current class
        # can also define attributes with the `self.attr` syntax
        self.alive = True
        self.spine = True
        self.lungs = True
        self.hair = False

    def move(self):
        return "Move a bit"

    def eat(self):
        return "Something"

    def breath(self):
        return "Oxygen"


# Example of an animal object
cat = Animal()
oriental_longhair = Animal()

oriental_longhair.hair = True # Polymorphism - overwriting class values according to our needs
print(oriental_longhair.hair)
