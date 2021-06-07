from weather_forecaster import WeatherForecastByPostcode


def main():
    print('Welcome!')
    while True:
        choice = input('Would you like to get a weather forecast? [y/n]\n')
        if choice.lower() in ['y', 'yes']:
            # instantiate Weather forecaster class
            wf = WeatherForecastByPostcode()
            # Get user input for postcode
            user_postcode = input('Please input a postcode:  ')
            # Get weather
            wf.weather_today(user_postcode)
            print()

        elif choice.lower() in ['n', 'no']:
            return


if __name__ == '__main__':
    main()
