import requests
import json 

api_key = '628b24e279558dc47b21fb160692cdcf'
location = input("Enter a location: ")

def weather_main(location):
   response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}')
   print(response.status_code)
   print(response.json())
   
weather_main(location)