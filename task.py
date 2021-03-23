
# As a user sell tickets accordign to the age of the user and category of the movie
# eg 12, 12a, PG, U, 15 and 18
# user input to get age - decide if ticket can be sold
# implement casting (display age back to user with appropriate message)

movies = [
        {'title': 'Star Wars', 'genre': 'Sci-Fi', 'age_rating': 15},
        {'title': 'Star Trek', 'genre': 'Sci-Fi', 'age_rating': 12},
        {'title': 'Lord of the Rings', 'genre': 'Fantasy', 'age_rating': 18},
        ]


while True:
    print('Please choose a movie')

    for id, movie in enumerate(movies):
        print(f"{id}) {movie.get('title')}")

    choice = input()
    if choice.isdigit() and int(choice) in range(len(movies)):
        movie_choice = movies[int(choice)]
        print(f"Movie: {movie_choice.get('title')}\n")
    else:
        print('Wrong choice. Try again')
        continue

    # Get customer age
    customer_age = input('Please input customer age:  ')
    customer_age = int(customer_age) if customer_age.isdigit() else None

    # Get allowed age
    allowed_age = int(movie_choice.get('age_rating'))

    if customer_age >= allowed_age:
        print(f'Your age is {customer_age}, you are welcome to buy tickets')

    elif customer_age < allowed_age:
        print(f'Your age is {customer_age}, you are not allowed to watch this film. The allowed age is {allowed_age}')
    # Handle None types
    else:
        print(f'Age provided was not appropriate. Please try again')

    # Spacers
    print()
    print()
