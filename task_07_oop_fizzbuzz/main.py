# TASK 7 - OOP FIZZBUZZ
# Author: Alexis
import random


class FizzBuzz():

    def __init__(self, maxnum=100):
        self.maxnum = maxnum
        self.numbers = list(range(1, maxnum))

    # Check if the numbers that were given are positive and nonzero
    def _check_number(self, value):
        try:
            if value.isdigit():
                # Cast to integer then perform the bound check
                return self._num_in_bounds(int(value))
            return False
        # Except an AttributeError if the value is an integer
        except AttributeError:
            return self._num_in_bounds(value)

    # Check if a number is within bounds (between 0 and maxnum)
    def _num_in_bounds(self, number):
        if number > 0 and number < self.maxnum:
            return True
        return False

    def fizzbuzzify(self, numA=3, numB=5):
        if not (self._check_number(numA) and self._check_number(numB)):
            print('Wrong inputs, cancelling operation')
            return
        self.numA = int(numA)
        self.numB = int(numB)

        for idx in self.numbers:
            temp = ('Fizz' if not idx % self.numA else '') + ('Buzz' if not idx % self.numB else '')
            # check if temp is empty
            if temp:
                self.numbers[idx-1] = temp
        self.show_numbers()

    def show_numbers(self):
        for items in self.numbers:
            print(items)

    def reset_numbers(self):
        self.numbers = list(range(1,maxnum))

    def __rep__(self):
        return f"Fizzbuzz list object"


if __name__ == '__main__':
    fizzy = FizzBuzz()
    numA = random.randint(1, 10)
    numB = random.randint(1, 10)
    print(f"Drawn numbers {numA} and {numB}")
    fizzy.fizzbuzzify(numA, numB)
