# TASK 10 - Your Hero Story

# 1. Define a dictionary called story, that includes the following keys: ('start', 'middle', 'end')
story = {
        'start': 'There once was a man that found a lamp.',
        'middle': 'He rubbed the lamp to reveal a genie',
        'end': 'The genie had zero powers and just hang out. The end.'
        }

# 2. Print the entire dictionary
print('\n\nPrinting the entire dictionary')
print(story)

# 3. Print the type of your dictionary
print('\n\nPrinting the type of dictionary')
print(type(story))

# 4. Print only the keys
print('\n\nPrinting only the keys')
print(story.keys())

# 5. Print only the values
print('\n\nPrinting only the values')
print(story.values())

# 6. Print the individual values using the keys (individually, lots of print commands)
print('\n\nPrinting individual values with the use of the keys')
for key in story.keys():
    print(story.get(key))

# 7. Finally, add a new key:value pair: `'hero': <your-super-hero>`
print('\n\nAdding the new key')
story.update({'hero': 'Aladdin'})
print(story)
