import requests
import json 

api_key = '628b24e279558dc47b21fb160692cdcf'
location = input("Enter a location: ")

def weather_main(location):
   response_current = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}')
   response_forecast = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={location}&units=metric&appid={api_key}')
   print(response_current.status_code)
   print(response_current.json())
   print(response_forecast.status_code)
   print(response_forecast.json())

weather_main(location)