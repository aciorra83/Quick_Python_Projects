import requests
# helps to format the JSON formatting we get from api site
from pprint import pprint

API_key = '67647fab6c0de384c7813d151913d53a'

city = input('Enter a city: ')

# where we send the response to
# 
base_url = 'https://api.openweathermap.org/data/2.5/weather?appid='+API_key+'&q='+city
weather_data = requests.get(base_url).json()

pprint(weather_data)