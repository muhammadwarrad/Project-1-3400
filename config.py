import requests
import pandas as pd;
import os


class Data:

    params = None
    info = None
    lat = None
    long = None
    
    def __init__(self,lat, long):
        self.lat = lat
        self.long = long
        self.params =  {
    "latitude": lat,
    "longitude": long,
    "current": ["temperature_2m", "relative_humidity_2m", "is_day", "precipitation", "rain", "weather_code", "wind_speed_10m"],
    "temperature_unit": "fahrenheit"
}
        
        dp = pd.DataFrame(self.getCurrentWeather())
        if not os.path.exists('output.csv'):
            # If the file does not exist, write the dataframe to a new CSV file

            dp.to_csv('output.csv', index=False, mode='w', header=True)
            print("output file")
            #
        else:
            # If the file exists, append the dataframe to the existing file

            dp.to_csv('output.csv', index=False, mode='a', header=False)
        #
        
    #
    url = "https://api.open-meteo.com/v1/forecast"

    def getCurrentWeather(self):
        # returns the dictionary for current weather
        self.response = requests.get(self.url, params=self.params)
        data = self.response.json()
        return pd.DataFrame(data['current'], index=[1])
    #
    def display_Weather(self):
        #Prints current weather conditions for given Location
        print(f"{self.getCurrentWeather()}")
    #
    
    
#






