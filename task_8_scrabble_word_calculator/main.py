# TASK 8 - Scrabble Word Count

# |Letter | Value |
# | --- | --- |
# |A,E,I,O,U,L,N,R,S,T | 1|
# |D, G | 2|
# |B, C, M, P | 3 |
# |F, H, V, W, Y | 4|
# |K | 5 |
# |J, X | 8 |
# |Q, Z| 10|
import scrabble


word = 'hello'
scoreboard = scrabble.ScrabbleScoreCounter()

scoreboard.show_scoring()

points = scoreboard.score_word(word)
print(f'The word {word} gets {points} points')
