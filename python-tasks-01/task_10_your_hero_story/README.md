# Your Hero Story!

> Timing: 30-50 Minutes

## Summary
You're going to write a story, cut it into sections and store the sections in a python dictionary!

## Tasks

1. Define a dictionary called story, that includes the following keys: ('start', 'middle', 'end')
2. Print the entire dictionary
3. Print the type of your dictionary
4. Print only the keys
5. Print only the values
6. Print the individual values using the keys (individually, lots of print commands)
7. Finally, add a new key-value pair: `'hero': <your-super-hero>`

## Acceptance Criteria
- All 7 tasks are done
- Runs with no errors
- Tells a story

## Solution

1. For the first  task, a simple dictionary was created with the keys *start*, *middle* and *end*, as shown below:
```python
story = {
        'start': 'There once was a man that found a lamp.',
        'middle': 'He rubbed the lamp to reveal a genie',
        'end': 'The genie had zero powers and just hang out. The end.'
        }
```

2. For the next task, a simple `print` statement was used to print the whole dictionary
```python
print(story)
```

3. The type of the dictionary can be easily found with the `type` method:
```python
print(type(story))
```

4. The keys are printed with the simple dictionary method `keys`
```python
print(story.keys())
```

5. On the other hand, the values of the dictionary can be selected with the dictionary method `values`
```python 
print(story.values())
```

6. We can print each value individually with the use of the keys by iterating through the list of keys that was returned with the `keys` method and use them to get the dictionary values.
```python
for key in story.keys():
    print(story.get(key))
```

7. A key-value pair can be easily added to an existing dictionary with the `update` method.
```print
story.update({'hero': 'Aladdin'})
print(story)
```

