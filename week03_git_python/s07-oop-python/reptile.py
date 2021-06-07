# import Animal class

from animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None
        self.hard_chambers = [3, 4]

    def hunt(self):
        return "Working hard to catch the next meal."

    def use_venom(self):
        return "I use it if I've got any"

    def seek_heart(self):
        return "Something"


# Let's see the benefits of inheritance.
# reptile_object = Reptile()
# 
# print(reptile_object.hunt())
# print(reptile_object.breath())
