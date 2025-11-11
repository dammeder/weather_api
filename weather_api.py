import datetime as dt 
import requests
import json 


with open('api_key', 'r') as f:
    API_KEY = f.read().strip()

CITY = input("What citys weather would you like to check: ")

URL = "https://api.openweathermap.org/data/2.5/weather"


params = {
    "q": CITY,
    "limit": 1,
    "appid": API_KEY
}


def kel_to_c_f(kelvin):
    celcius = kelvin - 273.15
    fahrenheit = celcius * (9/5) + 32

    return round(celcius, 2), round(fahrenheit, 2)


def temp_to_emoji(temp):
    if temp  <= 0: 
        return "⛄"
    elif 1 <= temp <= 10:
        return "❄️"
    elif 11 <= temp <= 15:
        return "🥶"
    elif 16 <= temp <= 20:
        return "🌥️"
    elif 21 <= temp <= 25:
        return "🌤️"
    elif 26 <= temp <= 30:
        return "☀️"
    elif temp > 30:
        return "🔥"


def desc_to_emoji(desc):
    if "clouds" in desc:
        return "☁️"
    elif "thunderstorm" in desc:
        return "⛈️⚡"
    elif "drizzle" in desc:
        return "🌦️"
    elif "rain" in desc:
        return "🌧️"
    elif "snow" in desc:
        return "❄️"
    elif "clear" in desc:
        return "☀️"
    else:
        return "🌫️"
    
# try , execpt --- if i dont get a response 
response = requests.get(URL, params=params).json()

city = response['name']
temp_kelvin = response['main']['temp']

temp_celsius, temp_fahrenheit = kel_to_c_f(temp_kelvin)

feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kel_to_c_f(feels_like_kelvin)

temp_emoji = temp_to_emoji(temp_celsius)

description = response['weather'][0]["description"]
desc_emoji = desc_to_emoji(description)

sunrise_time = (dt.datetime.fromtimestamp(response["sys"]["sunrise"], dt.timezone.utc) + dt.timedelta(seconds=response['timezone'])).strftime("%I:%M %p")
sunset_time = (dt.datetime.fromtimestamp(response["sys"]["sunset"], dt.timezone.utc) + dt.timedelta(seconds=response['timezone'])).strftime("%I:%M %p")

time = (dt.datetime.fromtimestamp(response["dt"], dt.timezone.utc) + dt.timedelta(seconds=response['timezone'])).strftime("%I:%M %p")

stamp_date = dt.datetime.now().strftime("%Y-%m-%d %H:%M")



print(f"\n\n\nTodays weather in {city} as of {time}:")
print(f"Tempature: {temp_celsius}C° / {temp_fahrenheit}F° {temp_emoji}")
print(f"Feels Like: {feels_like_celsius}C° / {feels_like_fahrenheit}F° {temp_emoji}")
print(f"Weather State: {description.title()} {desc_emoji}")
print(f"Sunrise: {sunrise_time}")
print(f"Sunset: {sunset_time}")


new_entry = {
    "timestamp": stamp_date,
    "temp_c": temp_celsius,
    "temp_f": temp_fahrenheit,
    "city": city
}

with open("weather_log.json", "r" ) as log:
    old_entry = json.load(log)

with open("weather_log.json", "w") as log: 
    json.dump(new_entry, log, indent=2)




# 🌤️ Todays weather in Huntley as of 08:25 PM:
# 🌡️ Tempature: 12.1C° / 53.7F°
# Feels Like: 10.4C° / 50.8F°
# Weather State: Overcast Clouds
# Sunrise: 06:33 AM
# Sunset: 04:41 P