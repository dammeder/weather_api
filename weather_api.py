import datetime as dt 
import requests


with open('api_key', 'r') as f:
    API_KEY = f.read().strip()
CITY = "Huntley"

URL = "https://api.openweathermap.org/data/2.5/weather"


params = {
    "q": CITY,
    "limit": 1,
    "appid": API_KEY
}


def kel_to_c_f(kelvin):
    celcius = kelvin - 273.15
    fahrenheit = celcius * (9/5) + 32

    return round(celcius, 1), round(fahrenheit, 1)


response = requests.get(URL, params=params).json()

# print(response)

city = response['name']
temp_kelvin = response['main']['temp']

temp_celsius, temp_fahrenheit = kel_to_c_f(temp_kelvin)

feels_like_kelvin = response['main']['feels_like']

feels_like_celsius, feels_like_fahrenheit = kel_to_c_f(feels_like_kelvin)

description = response['weather'][0]["description"].title()
sunrise_time = (dt.datetime.fromtimestamp(response["sys"]["sunrise"], dt.timezone.utc) + dt.timedelta(seconds=response['timezone'])).strftime("%I:%M %p")
sunset_time = (dt.datetime.fromtimestamp(response["sys"]["sunset"], dt.timezone.utc) + dt.timedelta(seconds=response['timezone'])).strftime("%I:%M %p")

time = (dt.datetime.fromtimestamp(response["dt"], dt.timezone.utc) + dt.timedelta(seconds=response['timezone'])).strftime("%I:%M %p")


print(f"\n\n\nTodays weather in {city} as of {time}: ")
print(f"Tempature: {temp_celsius}C° / {temp_fahrenheit}F°")
print(f"Feels Like: {feels_like_celsius}C° / {feels_like_fahrenheit}F°")
print(f"Weather State: {description}")
print(f"Sunrise: {sunrise_time}")
print(f"Sunset: {sunset_time}")


