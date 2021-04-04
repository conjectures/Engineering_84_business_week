# Import the reptile class

from reptile import Reptile


class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.limbs = False
        self.use_venom = True
        self.fork_tongue = True


    def use_tongue_to_smell(self):
        return "I use my tongue to smell the food"

    def shed_skin(self):
        return "growing out"

# snake_object = Snake()
# print(snake_object.shed_skin())
# print(snake_object.move())
