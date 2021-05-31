
# Create a function that takes inputs 'water' and 'flour' to return 'dough'
def make_dough(*args):
    # Check if 2 ingredients were passed
    if len(args) == 2:
        # Check if the ingredients that were passed are exactly 'water' and 'flour' in any order.
        if args[0] in ['water', 'flour'] and args[1] in ['water', 'flour'] and args[0] != args[1]:
            return 'dough'


# Create a function that takes as input 'dough' and returns 'bread'
def bake_dough(*args):
    # Check if only one ingredient is passed
    if len(args) == 1:
        # Check if that ingredient is 'dough'
        if args[0] == 'dough':
            return 'naan'


# Create a function that uses the functions 'make_dough' and 'bake_dough' to produce naans
def run_factory(*args):
    # Call make_dough to pass ingredients to bake_dough. Return result
    return bake_dough(make_dough(*args))


# Create a function that acts as a UI for a user who wants to create naans
def main():
    while True:
        # Ask for user choice to continue or exit
        choice = input("Run factory? [y/n]")
        # Check user choice
        if choice.lower() in ['y', 'yes']:
            # Ask for ingredients
            ingredient_01 = input("Ingredient 1? \n")
            ingredient_02 = input("Ingredient 2? \n")
            result = run_factory(ingredient_01, ingredient_02)
            # Check if resutl is not None
            if result:
                print(f'You get {result}!\n\n')
            # If result is none, print failure message
            else:
                print('You failed to make bread\n\n')
        # Handle exit condition
        elif choice.lower() in ['n', 'no']:
            print('Goodbye!\n')


if __name__ == '__main__':
    main()
