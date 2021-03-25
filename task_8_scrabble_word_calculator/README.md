# TASK 8 - Scrabble Word Calculator

## Summary
Create a Scrabble Word Calculator with OOP

## Tasks
Given the below scoring table, reate a Scrabble word calculator that will provide the correct scores, dependent on the string provided.

|Letter | Value |
| --- | --- |
|A,E,I,O,U,L,N,R,S,T | 1|
|D, G | 2|
|B, C, M, P | 3 |
|F, H, V, W, Y | 4|
|K | 5 |
|J, X | 8 |
|Q, Z| 10|


## Acceptance Criteria
- All tasks are done
- Core tasks work without errors

## Documentation
The Scrabble Scoring Program is located in the file `scrabble.py`. The file `main.py` showcases a typical usage of the library.

### Running the program
Run program with `python main.py`

### How to import
The library can be used by adding `import scrabble` in your script. The library includes a class called `ScrabbleScoreCounter` which can be used by instantiating, as shown below:
```python
import scrabble

scoring_program = scrabble.ScrabbleScoreCounter()
```

### How to use class
The class has several two methods, one to show the scoring policy, named `show_scoring`. This method takes no arguments.
The other class can be used to score a word. This method, the `score_word` method takes a single argument, wich should be a string. If it is not a string, the method will stop executing.


## Solution

The program works by creating a look-up dictionary with the values of each letter saved as a key-value pair.
The dictionary is created in the `__init__` method as shown below.

```python
class ScrabbleScoreCounter():

    def __init__(self):
        self.score_table = {
                **dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], 1),
                **dict.fromkeys(['D', 'G'], 2),
                **dict.fromkeys(['B', 'C', 'M', 'P'], 3),
                **dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 4),
                **dict.fromkeys(['K'], 5),
                **dict.fromkeys(['J', 'X'], 8),
                **dict.fromkeys(['Q', 'Z'], 10),
                }
```
To achieve code brevity, the function `dict.fromkeys` is used, which creates a dictionary with the keys provided and with all of them having the same value.
The aforementioned function is very useful in our use case, since a lot of the letters have the same value.
Then, the different dictionaries are combined by unpacking them and adding them in the same dictinary, as shown below in a more simple example:

```python
# define a simple dictionary with a single value
a = {'a': 1}
# define another dictionary with two entries
b = { 'b':2, 'B':3 }

# By unpacking the dictionary, each entry 'comes out' of it's curly brackets and can is then recombined with theother entries:
c = { **a, **b }
# c = { 'a':1, 'b':2, 'B':3 }
```

```python
    def score_word(self, word):
        if not isinstance(word, str):
            print('Not a word.')
            return
        # Initialise scoring var
        total = 0
        # Traverse word
        for letter in word:
            # Get values from scoring dictionary
            value = self.score_table.get(letter.upper())
            # Add value if it is not None
            total = total+value if value else total
        return total

    # Method that prints the internal
    def show_scoring(self):
        for key, value in self.score_table.items():
            print(f'{key} gets {value} points.')

```
