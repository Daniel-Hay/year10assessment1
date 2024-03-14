import requests
import json
from rich.table import Table
from rich.console import Console
import time

api_key = '628b24e279558dc47b21fb160692cdcf'
history = []

print("Welcome to Daniel's Weather Console")

def intro():
   answer = input("Do you want to continue (c), view instruction (i) or exit the program (e)")
   if answer == "c":
      weather_main(location = input("Enter a location: "))
   elif answer == "i":
      intructions()
   elif answer == "e":
      exit()
   else:
      print("Enter either (c), (i) or (e)")
      time.sleep(2)
      intro()

# Main function with current weather, 5 day forecast and error handling
def weather_main(location):

   # Data Requests to API
   response_current = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}') 
   response_forecast = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={location}&units=metric&appid={api_key}')

   # Checks if the location is a valid value
   if response_current.status_code == 200: 

      current_weather = json.loads(response_current.text)
      forecast_weather = json.loads(response_forecast.text)

      # Adding to the history list
      history.append(location)

      print(current_weather['main']['temp']) 

      # print(response_current.status_code)
      # print(response_current.json())
      # print(response_forecast.status_code)
      print(response_forecast.json())

      # prints current weather
      print(f"The current weather in {location}")
      print(f"History: ")
      print(history)

      def forecast(location):
         forecasttable = Table(title="5 Day Forecast")
         forecasttable.add_column(" ")
         forecasttable.add_column(location, style="magenta")

         forecasttable.add_row("temperature", forecast_weather['list'][1]['main']['temp'])

         console = Console()
         console.print(forecasttable)

      forecast(location)

   # If invalid request, re-asks user to input a valid location
   else:
      print("Status denied")
      location_new = input("Re-enter a location: ")
      weather_main(location_new)

def intructions():
   intro()

intro()