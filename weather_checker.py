import os
import requests


api_key = os.environ['key']

city_name = input("Enter city name here: ")
units = "metric"
api_call = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units={units}&appid={api_key}"
req = requests.get(api_call)
convert = req.json()

#print(convert)
weather = convert["weather"][0]["main"]
temp = convert["main"]["temp"]
humidity = convert["main"]["humidity"]
print()
print(f"Weather: {weather} \nTemperature: {temp} C \nHumidity: {humidity}")
    
    
    
