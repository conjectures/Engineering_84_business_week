# TASK 5 - Functional Calculator

## Summary
Amazing you now know functions, lets make a functional calculator.

## Objectives
- Practice using, defining and calling functions
- Build a basic functional calculator

## Tasks
**_Core:_**
1. Build a function containing:
  - Add
  - Subtract
  - Multiply
  - Divide

2. Buld more functions for 
  - Area of a circle
  - Area of a square
  - Area of a triangle

**_Extra:_**
- Run function with arguments
- Assert against known values. Adding 10+30 will alwyas be 40
```python
# example
def add_function(arg1, arg2):
  return arg1 + arg2


print("calling the add_function() with 290 and 10, expect 300 to be the result ")
print(add_funtion(290, 10) == 300)
print('got:', add_funtion(290, 10) )

print("calling the add_function() with 270 and 5, expect 275 to be the result ")
print(add_funtion(270, 5) == 275)
print('got:', add_funtion(270, 5) )
```

*Hint*: Do one function at a time. And use my structure for running the functions


## User Stories
-  As a user I want to have a add_funtion() that takes in two arguments and adds them.

## Acceptance Criteria
- All core tasks done
- Separation of concerns if followed
- Dry code and functions
