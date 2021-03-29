# Task 1: TDD Bread Factory
> Time: 30-45 Minutes

## Summary
TDD bread factory is the latest bread brand in Py Land.
It always produces the best bread because it has the best testing strategy!
What they do is before they make any new bread, they make a test to make sure the end ouput is correct.
Then they adjust the recipe until it's just right!

You are going to do the same with bread! This is called Test Driven Development.

## Tasks
This exercise is going to bring together lots of concepts.
### Learning Outcomes
- Git & Github
- Functions
- TDD
- Separation of concerns (important do not ignore!)
- DRY code
- DOD (Definition of Done)

### Intalling and running
To run the naan factory do the following:

import naan_factory
run_factory()
TDD - test driven development
write the test
run it, and read the error
code and make it pass the test
this helps with:
- Stop over engineering
- Maintainable code
- Reduce technical debt
- Goes well with agile and working code
- errors can be your guide in complex systems

How it works is that we write unit tests.

Unit Tests
Test single pieces of code. Like a function.

base of a test
Usually has 3 phases.
- setup phase (know variables)
- calling of the function / piece of code with know variables
- asserting for expect output

User stories for Naan Factory
#1
As a user, I can use the make dough with 'water' and 'flour' to make 'dough'.

#2
As a user, I can use the bake dough with dough to get naan.

#3
As a user, I can user the run factory with water and flour and get naan.
Acceptance Criteria
you have written tests
test pass
you have written more test to make sure everything works as indented
all user stories are satisfied
code does not break
code has exit condition
DOD if followed
