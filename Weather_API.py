import requests  # Importing the requests module which allows HTTP requests

class City:
    def __init__(self, name, lat, lon, units="metric"):
        # Constructor method, initializes attributes when a City object is created
        self.name = name  # City name
        self.lat = lat    # Latitude of the city
        self.lon = lon    # Longitude of the city
        self.units = units  # Preferred units for temperature (default is metric)
        self.get_data()    # Calling get_data method to fetch weather data

    def get_data(self):
        # Method to fetch weather data from OpenWeatherMap API
        try:
            # Sending an HTTP GET request to the OpenWeatherMap API to get weather data
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=4717ab6e02c260388a903c16635216d1")
        except:
            # If there's an exception (e.g., no internet connection), print an error message
            print("No internet :(")

        # Parsing the JSON response
        self.response_json = response.json()  # Storing the JSON response in an attribute
        self.temp = self.response_json["main"]["temp"]  # Current temperature
        self.temp_min = self.response_json["main"]["temp_min"]  # Minimum temperature
        self.temp_max = self.response_json["main"]["temp_max"]  # Maximum temperature

    def temp_print(self):
        # Method to print temperature information
        units_symbol = "C"  # Default units symbol (Celsius)
        if self.units == "imperial":
            units_symbol = "F"  # If units are imperial, change units symbol to Fahrenheit
        print(f"In {self.name} it is currently {self.temp}° {units_symbol}")
        print(f"Today's High: {self.temp_max}° {units_symbol}")
        print(f"Today's Low: {self.temp_min}° {units_symbol}")

# Creating instances of the City class
my_city = City("Tokyo", 35.6764, 139.6500)  # Using default units (metric)
my_city.temp_print()  # Printing temperature information for Tokyo

# Creating another instance with different units
vacation_city = City("Portland", 45.5152, -122.6784, units="imperial")  # Using imperial units
vacation_city.temp_print()  # Printing temperature information for Portland

# Accessing the JSON response directly (for demonstration purposes)
print(vacation_city.response_json)