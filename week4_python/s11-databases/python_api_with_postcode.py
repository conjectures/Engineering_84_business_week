# API for postcode.io

import requests

url = "https://api.postcodes.io/postcodes/"
postcode = 'e147le'

urlarg = url + postcode
print(urlarg)

response = requests.get(urlarg)
result = response.json().get('result')


print(f"Your postcode location is {result.get('postcode')}")
print(f"Your country is {result.get('country')}")
