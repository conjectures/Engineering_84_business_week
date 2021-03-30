# TASK: Weather forecast program that uses APIs to get weather for specific Postcode (UK)
# Author: Alexis
import requests


class WeatherForecastByPostcode():

    def __init__(self):
        pass

    def get_city_from_postcode(self, postcode):
        url = "https://api.postcodes.io/postcodes/"
        post_request = requests.get(url+postcode)
        if post_request:
            result = post_request.json().get('result')
            return result.get("parliamentary_constituency")
        return None

    def get_lattlong_from_postcode(self, postcode):
        url = "https://api.postcodes.io/postcodes/"
        post_request = requests.get(url+postcode)
        # if post_request.status_code:
        if post_request:
            result = post_request.json().get('result')
            return result.get('latitude'), result.get('longitude')
        return None

    # lattlong to woeid
    def get_woeid_from_lattlong(self, *args):
        url = 'https://www.metaweather.com/api/location/search/?lattlong='
        args = ','.join(map(str, args))
        urlargs = url + args
        woeid = requests.get(urlargs)
        # Request object will evalueate to True if status code is < 400
        if woeid:
            # API returns dictionary in list:
            result = woeid.json()[0].get('woeid')
            return result
        return None

    # woeid to weather
    def get_weather_from_woeid(self, woeid):
        # woeid for london
        weather = requests.get(f'https://www.metaweather.com/api/location/{woeid}')
        # Request object will evalueate to True if status code is < 400
        if weather:
            # First index in list is for today
            self.weather_today = weather.json().get('consolidated_weather')[0]
            return self.weather_today
        return None

    def weather_today(self, postcode):
        today = self.get_weather_from_woeid(self.get_woeid_from_lattlong(*self.get_lattlong_from_postcode(postcode)))

        area = self.get_city_from_postcode(postcode)
        state = today.get('weather_state_name')
        min_temp = today.get('min_temp')
        max_temp = today.get('max_temp')
        the_temp = today.get('the_temp')

        print(f"Today, the weather {area} is {state}.\nThe temperature is {the_temp}C with a high of {round(max_temp, 2)}C and a low of {round(min_temp, 2)}C")

    def __repr__(self):
        return f'Weather Forecast class'


def main():
    wf = WeatherForecastByPostcode()
    wf.weather_today('sw109uu')


if __name__ == '__main__':
    main()
