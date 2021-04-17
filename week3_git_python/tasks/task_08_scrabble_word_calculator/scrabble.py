# TASK 8 - Scrabble Counter

# Scrabble Score Counter Library

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

