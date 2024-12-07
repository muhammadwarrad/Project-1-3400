'''
Authors:
<***>
Date Created: <***>
Date Last Updated: <***>
Doc:
<***>
Notes:
<***>
'''

#IMPORTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
import requests
import pandas as pd
import urllib.parse
import numpy as np
from config import LOGGING_CONFIG
import logging, logging.config
from config import API_CONFIG
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger()
params = API_CONFIG["params"]
#%% USER INTERFACE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#%% CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#%% CONFIGURATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#%% INITIALIZATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#%% DECLARATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Global declarations Start Here
#Class definitions Start Here
class Data:
    def __init__(self, latitudes, longitudes):
        self.latitudes = latitudes  # List of latitudes
        self.longitudes = longitudes  # List of longitudes
        try: 
            weather_data = self.getCurrentWeather()
            self.save_to_csv(weather_data)
        except Exception as e:
            logger.error(f"Data could not be retrieved {e}")

    def getCurrentWeather(self):
        # Get weather data for all locations
        weather_data = []
        for lat, lon in zip(self.latitudes, self.longitudes):
            # Manually encode the latitude and longitude to ensure proper formatting
            params["latitude"] = np.array(lat)
            params["longitude"] = np.array(lon)
            
            # Manually construct the query string and encode it
            query_string = urllib.parse.urlencode(params)
            full_url = f"{API_CONFIG['url']}?{query_string}"
            
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
                    del current_weather['interval']
                    current_weather['latitude'] = lat
                    current_weather['longitude'] = lon
                    weather_data.append(current_weather)
                else:
                    logger.warning(f"No current weather data found for {lat}, {lon}")
                
            except requests.exceptions.RequestException as e:
                logger.error('%s raised an error', {e})
        
        return weather_data

    def save_to_csv(self, weather_data):
        # Convert the weather data to a pandas DataFrame
        if weather_data:
            df = pd.DataFrame(weather_data)

            # Check if the output file exists and append or write accordingly
            if not os.path.exists('Data.csv'):
                df.to_csv('Data.csv', index=False, mode='w', header=True)
                logger.info("Creating new Data.csv")
            else:
                df.to_csv('Data.csv', index=False, mode='a', header=False)
                logger.info("Appending to Data.csv")
        else:
            logger.warning("No weather data")

#%% MAIN CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main code start here
if __name__ == "__main__":
    print(f"\"{__name__}\" module begins.")
    
    # Example usage of Data class with latitudes and longitudes
    latitudes = [37.7749, 34.0522, 40.7128]  # Example latitudes (San Francisco, Los Angeles, New York)
    longitudes = [-122.4194, -118.2437, -74.0060]  # Example longitudes
    
    # Initialize the Data class to fetch weather data
    data = Data(latitudes, longitudes)
    
#%% SELF-RUN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main Self-run block

