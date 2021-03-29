
def make_dough(*args):
    if len(args) == 2:
        if args[0] in ['water', 'flour'] and args[1] in ['water', 'flour'] and args[0] != args[1]:
            return 'dough'


def bake_dough(*args):
    if len(args) == 1:
        if args[0] == 'dough':
            return 'naan'


def run_factory(*args):
    return bake_dough(make_dough(*args))


def main():
    while True:
        choice = input("Run factory? [y/n]")
        if choice.lower() in ['y', 'yes']:
            ingredient_01 = input("Ingredient 1? \n")
            ingredient_02 = input("Ingredient 2? \n")
            result = run_factory(ingredient_01, ingredient_02)
            if result:
                print(f'You get {result}!\n\n')
            else:
                print('You failed to make bread\n\n')
        elif choice.lower() in ['n', 'no']:
            print('Goodbye!\n')


if __name__ == '__main__':
    main()
