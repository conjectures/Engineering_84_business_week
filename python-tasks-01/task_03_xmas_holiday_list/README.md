# TASK 3 - Xmas Holiday List

## Summary
Amazing, you've learner about the for loop!
Time to use that, plush a while loop to keep things going!
Your task is to create a list of xmas gifts using cool control flow now!
Read the task for the user stories.
**hint: While loops and break conditions, use lists and append, iterate to print**

## User stories
1. as a user, i want to be able to add items to the list, so I can read it later.
2. as a user, I want to be able to keep adding things to the list until I use exit
3. as as user, I should be able to use the word exit in a sentence and still have the program terminate, so that anyone can use it
4. as a user, when the program exits, I want to see the complete list in caps lock and numbered, so that I know what to buy. example:
  - 1. RC car
  - 2. PS2
  - 3. GTA Vice City

## Acceptance Criteria
- All user stories are completed
- Has documentation

## Documentation
Run the program with `python main.py`, or `python3` according to python version. 
**The program uses python 3.7++**

The program first starts by asking the user for items he would like for Christmas
```python
print("What would you like this Christmas? (write 'exit to stom program')")
```
The program will continue to ask for items until the user writes `exit` in the prompt (not case sensitive)

Finally, the whole list will be printed in the end:
```python
What i need to buy:
  1. PLANE
  2. BOAT
  3. SHIRT
  4. SOCKS
```


## Solution
Initially, the christmas list is declared as an empty list:
```python
christmas_list = []
```
Then, inside an infinite loop, the program asks for items from the user:
```python
    wish = input()
```

The program checks if the wish input was equal to the work 'exit' to stop executing the program
```python
    if wish.lower() == 'exit':
        break
```

If all is well, the item is appended to the list, and a new loop executes.
```python
    christmas_list.append(wish)
```
On the other hand, if the exit criteria for the loop is met, the program will loop through the list up to this point and print all the items in uppercase:
```python
for idx, item in enumerate(christmas_list):
    print(f"  {idx+1}. {item.upper()}")
```
