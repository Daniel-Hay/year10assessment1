import requests
import json
from rich.table import Table
from rich.console import Console
from rich import print
import time

api_key = '628b24e279558dc47b21fb160692cdcf'
history = []

print("Welcome to Daniel's Weather Console")

# Runs at the beginning of the program
def intro():
   answer = input("Do you want to continue (c), view instruction (i) or exit the program (e): ")
   if answer == "c":
      weather_main(location = input("Enter a location: "))
   elif answer == "i":
      intructions()
   elif answer == "e":
      exit()
   else:
      print("[bold red]Enter either (c), (i) or (e)[/bold red]")
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

      print(current_weather)

      print(f"The current weather in {location}")
      
      # Current weather function
      def current(location, current_weather):
         
         # Creates table for current weather
         currenttable = Table(title=f"Current Weather for {location.upper()}")
         currenttable.add_column(f"{location.upper()}", justify="center")
         currenttable.add_column(f"Current Weather")

         currenttable.add_row("Description", str(current_weather['weather'][0]['description']))
         currenttable.add_row("Temperature", str(current_weather['main']['temp']))
         currenttable.add_row("Feels Like", str(current_weather['main']['feels_like']))
         currenttable.add_row("Pressure", str(current_weather['main']['pressure']))
         currenttable.add_row("Humidity", str(current_weather['main']['humidity']))

         print(currenttable)

      # Forecast function for 5 day
      def forecast(location, forecast_weather):
         
         # Creates table for 5 day forecast weather
         counter_forecast = 1
         
         forecasttable = Table(title=f"5 Day Forecast for {location.upper()}")
         forecasttable.add_column(f"{location.upper()}", justify="center")

         while counter_forecast < 6:
            temperature_forcast0 = 0
            forecasttable.add_column(f"Day {counter_forecast}", style="magenta")
            counter_forecast += 1

         # Creates forecast table
         forecasttable.add_row("temperature", str(forecast_weather['list'][1]['main']['temp']), str(forecast_weather['list'][2]['main']['temp']), str(forecast_weather['list'][3]['main']['temp']), str(forecast_weather['list'][4]['main']['temp']), str(forecast_weather['list'][5]['main']['temp']))

         console = Console()
         console.print(forecasttable)

      current(location, forecast_weather)
      forecast(location, current_weather)

      # Adding to the history list
      history.append(location)
      print(f"History: {history}")

      # Re-asks user if they want to continue
      intro()

   # If invalid request, re-asks user to input a valid location
   else:
      print("[bold red]Status denied[/bold red]")
      location_new = input("Re-enter a location: ")
      weather_main(location_new)

def intructions():
   intro()

intro()