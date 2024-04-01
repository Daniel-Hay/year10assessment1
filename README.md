# Software Engineering Assessment 1 - Weather Console App

**Product Description:**
This Weather Console App utilises data obtained from _OpenWeather_ api's to create a seemless user experience in which they can input their wanted location to view the current and forecasted weather. The current weather data provides multiple differing analytics such as temperature, description, pressure and humidity whilst the 5 day forcast only provides the upcoming temperature.

---

**How to use:**
To use this program, run the python files then follow the different commands on the console depending on what option to choose. If you want to search up a certain location, type '_c_' then hit 'enter', to view further instructions, type '_i_' then hit enter, and to exit the program, type '_e_' then hit enter. The weather searching function only allows for suburbs, cities, states and countries but not specific addresses. If you dont input a valid request, the program will ask you if you would like to enter a different location (press _l_ then enter) or return to the menu (press _any other key_ then enter). Once you request a valid location, the console will repeat and ask you if you would like to search for a different location, view menu or exit. 


**Packages/Libraries Used:**
* rich, version 13.7.1
* requests, version 2.25.1
* json (standard library)
* time (standard library)
* os (standard library)
