
from snake import Snake


class Python(Snake):

    def __init__(self):
        super().__init__()

        self.large = True
        self.two_lungs = True


    def climb(self):
        return "up we go"

    def swallow(self):
        return "can't be bothered"

python_object = Python()

print(python_object.climb())
print(python_object.use_tongue_to_smell())
print(python_object.hunt())
