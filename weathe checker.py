import os
import requests

api_key = "fb61880be0dfdfdba64215274e5d3398"
#api_key = os.environ['key'] #(replit env file)

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
    
    
    
