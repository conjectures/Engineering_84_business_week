#TASK 3
# Author: Alexis
"""
    1. as a user, i want to be able to add items to the list, so I can read it later.
    2. as a user, I want to be able to keep adding things to the list until I use exit
    3. as as user, I should be able to use the word exit in a sentence and still have the program terminate, so that anyone can use it
    4. as a user, when the program exits, I want to see the complete list in caps lock and numbered, so that I know what to buy. example:
      - 1. RC car
      - 2. PS2
      - 3. GTA Vice City
"""

# Initialise list
christmas_list = []

# Give context & directions
print("What would you like this Christmas? (write 'exit to stom program')")
# Create infinite loop
while True:
    # Get user input
    wish = input()
    # Check if input was 'exit' without case sensitivity
    if wish.lower() == 'exit':
        # if input was exit, stop the loop
        break
    # Append item to list
    christmas_list.append(wish)
    # Ask for new item
    print("Noted. What else?")


print("\n\nWhat i need to buy:")
# Print full list
for idx, item in enumerate(christmas_list):
    print(f"  {idx+1}. {item.upper()}")
