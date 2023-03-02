import os
import requests

#api_key = "____________________" #You can get your own key at OpenWeather
api_key = os.environ['key'] #Replit system environment variables(secret key only you can access
continent = input("Enter continent: ")
city_name = input("Enter city name here: ")

def weather():
  units = "metric"
  
  api_call = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units={units}&appid={api_key}"
  req = requests.get(api_call)
  convert = req.json()
  weather = convert["weather"][0]["main"]
  temp = convert["main"]["temp"]
  humidity = convert["main"]["humidity"]
  print()
  print(f"Weather: {weather} \nTemperature: {temp} C \nHumidity: {humidity}")

def time():
  city = city_name.replace(" ", "_")
  api_time = f"https://www.timeapi.io/api/Time/current/zone?timeZone={continent}/{city}"
  time_data = requests.get(api_time)
  r = time_data.json()
  time = r["time"]
  print(f"Time: {time}")


weather()
time()
    
    
    
