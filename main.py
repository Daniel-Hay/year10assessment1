import requests
import json
from rich import print
from rich.console import Console
from rich.theme import Theme

# Custom Styles
wrong_theme = Theme({"success": "green", "error": "red"})


api_key = '628b24e279558dc47b21fb160692cdcf'
location = input("Enter a location: ")
history = []


def intro():
   print("Welcome to Daniel's Weather Console")


# Main function with current weather, 5 day forecast and error handling
def weather_main(location):

   # Data Requests to API
   response_current = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}') 
   response_forecast = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={location}&units=metric&appid={api_key}')

   # Checks if the location is a valid value
   if response_current.status_code == 200: 

      current_weather = json.loads(response_current.text)
      forecast_weather = json.loads(response_forecast.text)

      print(current_weather['main']['temp']) 

      # print(response_current.status_code)
      # print(response_current.json())
      # print(response_forecast.status_code)
      # print(response_forecast.json())

      # prints current weather
      print(f"The current weather in {location}")

   # If invalid request, re-asks user to input a valid location
   else:
      Theme.print("Status denied", style = "error")
      location_new = input("Re-enter a location: ")
      weather_main(location_new)


weather_main(location)
