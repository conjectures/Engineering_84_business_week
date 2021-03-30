import requests

class WeatherForecaster():

    def __init__(self):
        self.site = 'https://www.theweatheroutlook.com/forecast/uk'
        self.postcode_site = ''

    def postcode_to_lattlong(self, postcode):
        url = "https://api.postcodes.io/postcodes/"
        post_request = requests.get(url+postcode)
        # if post_request.status_code:
        print(post_request.status_code)
        # .json().get('result')
        result = post_request.json().get('result')
        return result.get('latitude'), result.get('longitude')

    # lattlong to woeid
    def woeid_from_lattlong(self, *args):
        url = 'https://www.metaweather.com/api/location/search/?lattlong=50.068,-1.316'
        urlargs = 




    # woeid to weather
    def get_weather_from_woeid(self):
        # woeid for london
        weather = request.get('https://www.metaweather.com/api/location/44418/')
        return weather.json()

        


def main():
    wf = WeatherForecaster()
    location = wf.postcode_to_lattlong('bh91bj')
    print(location)


if __name__ == '__main__':
    main()
