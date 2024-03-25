# Imports all necessary librarys and modules
import requests
import json
from rich.table import Table
from rich import print
import time
import os

api_key = 'b7ce39c80b01f1c963aac26c38d516e8'
history = []

print("Welcome to Daniel's Weather Console")

# Runs at the beginning of the program
def intro():
   # Asks user what option they want to select
   answer = input("Do you want to continue (c), view instruction (i) or exit the program (e): ")
   answer = answer.lower()
   if answer == "c":
      weather_main(location = input("Enter a location: "))
   elif answer == "i":
      intructions()
   elif answer == "e":
      os.system('cls')
   else:
      print("[bold red]Enter either (c), (i) or (e)[/bold red]")
      time.sleep(2)
      intro()

# Current weather function, takes in location and current weather data
def current(location, current_weather):
         
         # Creates table for current weather
         currenttable = Table(title=f"Current Weather for {location.upper()}")
         currenttable.add_column(f"{location.upper()}", justify="center")
         currenttable.add_column(f"Current Weather")

         # Creates the rows for the current weather
         currenttable.add_row("Description", str(current_weather['weather'][0]['description']))
         currenttable.add_row("Temperature", str(current_weather['main']['temp']))
         currenttable.add_row("Feels Like", str(current_weather['main']['feels_like']))
         currenttable.add_row("Pressure", str(current_weather['main']['pressure']))
         currenttable.add_row("Humidity", str(current_weather['main']['humidity']))

         # Outputs the current weather table on the console
         print(currenttable)

# Forecast function for 5 day, takes in location and forcast weather
def forecast(location, forecast_weather):
         
   # Creates table for 5 day forecast weather
   counter_forecast = 1
         
   forecasttable = Table(title=f"5 Day Forecast for {location.upper()}")
   forecasttable.add_column(f"{location.upper()}", justify="center")

   # Creates the 5 day columns for temperature
   while counter_forecast < 6:
      temperature_forcast0 = 0
      forecasttable.add_column(f"Day {counter_forecast}", style="magenta")
      counter_forecast += 1

   # Creates forecast rows for temperature data
   forecasttable.add_row("Temperature", str(forecast_weather['list'][1]['main']['temp']), str(forecast_weather['list'][2]['main']['temp']), str(forecast_weather['list'][3]['main']['temp']), str(forecast_weather['list'][4]['main']['temp']), str(forecast_weather['list'][5]['main']['temp']))

   # Outputs the forecast table onto the console
   print(forecasttable)

# Main function with current weather, 5 day forecast and error handling
def weather_main(location):

   # Data Requests to API
   response_current = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}') 
   response_forecast = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={location}&units=metric&appid={api_key}')

   # Checks if the location is a valid value
   try:
      # Parses Json into dictionary
      current_weather = json.loads(response_current.text)
      forecast_weather = json.loads(response_forecast.text)

      # Calls upon the current and forecast functions with location requested and respective data
      current(location, current_weather)
      forecast(location, forecast_weather)

      # Adding to the front of the history list
      history.insert(0, location)
      print(f"History: {history}")

      # Re-asks user if they want to continue
      intro()

   # If invalid request, re-asks user to input a valid location
   except:
      print("[bold red]Status denied, enter a valid location... or return to menu[/bold red]")
      # Asks user if they want to return to menu or enter new location
      denied_status = input("Re-enter location (l) or return to menu (m)")
      denied_status = denied_status.lower()
      if denied_status == 'l':
         weather_main(input("Re-enter a location: "))
      elif denied_status == 'm':
         intro()
      
# Callable function for intructions
def intructions():
   print("To search for the weather and 5 day forcast in a specific location, press c to continue and input the valid name of the location (either suburb, city or country)")
   time.sleep(2)
   print("To exit the program, press e")
   time.sleep(1)
   intro()

# Calls the intro function
intro()