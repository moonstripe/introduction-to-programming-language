# load_dotenv() takes our .env file and makes it accessible
from dotenv import load_dotenv

# the os module allows us to access our environmental variables
import os

# the request module gives us access to a lot of useful methods making requests
import requests

load_dotenv()

print('Input city name')
city_name = input()
print('Preferred units (C or F)')
units = input()

# city_name = 'Atlanta'

city_base = 'http://api.openweathermap.org/geo/1.0'
city_endpoint = '/direct'
city_params = f'?q={city_name}&appid={os.getenv("WEATHER_API_KEY")}'

city_response = requests.get(f'{city_base}{city_endpoint}{city_params}')
city_json = city_response.json()

# print(city_json)

latlong = (city_json[0]['lat'], city_json[0]['lon'])

# print(f'Coordinates: {latlong}')
def convert_k_to_f(kelvin):
    return round(1.8*(int(kelvin)-273) + 32, 2)

def convert_k_to_c(kelvin):
    return round(kelvin-273)

weather_base = 'https://api.openweathermap.org/data/2.5'
weather_endpoint = '/forecast'
weather_params = f'?lat={latlong[0]}&lon={latlong[1]}&appid={os.getenv("WEATHER_API_KEY")}'

weather_response = requests.get(f'{weather_base}{weather_endpoint}{weather_params}')
weather_json = weather_response.json()
weather_json_list = weather_json['list']

for forecast in weather_json_list:
    nth_forecast_item = forecast

    nth_forecast_time = nth_forecast_item['dt_txt']
    if units == 'F':
        nth_forecast_temp = f"{convert_k_to_f(float(nth_forecast_item['main']['temp']))}°F"
    else:
        nth_forecast_temp = f"{convert_k_to_c(float(nth_forecast_item['main']['temp']))}°C"
    nth_forecast_weather = nth_forecast_item['weather'][0]['main']

    print(f"""
Forecast Time: {nth_forecast_time}
Forecast Temperature: {nth_forecast_temp}
Forecast Weather: {nth_forecast_weather}
    """)
