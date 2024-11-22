import requests
import pandas as pd
import os
import urllib.parse
from log_config import logger


class Data:
    def __init__(self, latitudes, longitudes):
        self.latitudes = latitudes  # List of latitudes
        self.longitudes = longitudes  # List of longitudes
        self.url = "https://api.open-meteo.com/v1/forecast"
        try: 
            weather_data = self.getCurrentWeather()
            self.save_to_csv(weather_data)
        except Exception as e:
            logger.error("Data could not be retrieved", {e})
            

    def getCurrentWeather(self):
        # Get weather data for all locations
        weather_data = []
        for lat, lon in zip(self.latitudes, self.longitudes):
            # Manually encode the latitude and longitude to ensure proper formatting
            params = {
                "latitude": lat,
                "longitude": lon,
                "current_weather": "true",
                "temperature_unit": "fahrenheit"
            }
            
            # Manually construct the query string and encode it
            query_string = urllib.parse.urlencode(params)
            full_url = f"{self.url}?{query_string}"
            
            # Print the full URL to check how it looks
            print(f"Requesting: {full_url}")
            
            try:
                # Make the request to Open Meteo API
                response = requests.get(full_url)
                
                
                # Check for a successful response (200 OK)
                response.raise_for_status()
                
                # Parse the JSON response
                data = response.json()
                
                # Check if 'current_weather' is in the response
                if 'current_weather' in data:
                    current_weather = data['current_weather']
                    current_weather['latitude'] = lat
                    current_weather['longitude'] = lon
                    weather_data.append(current_weather)
                #
                else:
                    print(f"No current weather data found for {lat}, {lon}")
                    logger.warning("No current weather data found for {lat}, {lon}")
                #
            #
            except requests.exceptions.RequestException as e:
                logger.error('%s raised an error', {e})
                print(f"Request failed for {lat}, {lon}: {e}")
            #
        #
        
        return weather_data
    #

    def save_to_csv(self, weather_data):
        # Convert the weather data to a pandas DataFrame
        if weather_data:
            df = pd.DataFrame(weather_data)

            # Check if the output file exists and append or write accordingly
            if not os.path.exists('output.csv'):
                df.to_csv('output.csv', index=False, mode='w', header=True)
                logger.info("Creating new output.csv")
                print("Creating new output.csv")
            #
            else:
                df.to_csv('output.csv', index=False, mode='a', header=False)
                logger.info("Appending to output.csv")
                print("Appending to output.csv")
            #
        #
        else:
            print("No weather data to save.")
            logger.warning("No weather Data")
        #
    #


