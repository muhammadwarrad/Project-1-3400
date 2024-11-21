
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configure matplotlib for non-interactive backend
import matplotlib
matplotlib.use('Agg')

def create_sample_weather_data():
    np.random.seed(42)
    cities = ['New York', 'Boston', 'Miami']
    data = []
   
    for city in cities:
        if city == 'Miami':
            temps = np.random.normal(28, 3, 24)
        else:
            temps = np.random.normal(20, 5, 24)
           
        humidity = np.random.normal(70, 10, 24)
        precip = np.random.exponential(1, 24)
       
        city_data = pd.DataFrame({
            'city': city,
            'temperature': temps,
            'humidity': humidity,
            'precipitation': precip
        })
        data.append(city_data)
   
    return pd.concat(data, ignore_index=True)

def plot_temp_distribution(weather_df):
    plt.figure(figsize=(10, 8))
    cities = weather_df['city'].unique()
    data = [weather_df[weather_df['city'] == city]['temperature'] for city in cities]
    plt.boxplot(data, labels=cities)
    plt.title('Temperature Distribution by City')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.savefig('temperature_distribution.png', format='png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_precip_distribution(weather_df):
    plt.figure(figsize=(10, 8))
    cities = weather_df['city'].unique()
    data = [weather_df[weather_df['city'] == city]['precipitation'] for city in cities]
    plt.boxplot(data, labels=cities)
    plt.title('Precipitation Ranges')
    plt.ylabel('Precipitation (mm)')
    plt.xticks(rotation=45)
    plt.savefig('precipitation_distribution.png', format='png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_temp_humidity(weather_df):
    plt.figure(figsize=(10, 8))
    for city in weather_df['city'].unique():
        city_data = weather_df[weather_df['city'] == city]
        plt.scatter(city_data['temperature'], city_data['humidity'], label=city, alpha=0.5)
    plt.title('Temperature vs Humidity')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Humidity (%)')
    plt.legend()
    plt.savefig('temp_humidity_scatter.png', format='png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    weather_df = create_sample_weather_data()
    plot_temp_distribution(weather_df)
    plot_precip_distribution(weather_df)
    plot_temp_humidity(weather_df)
    print("All plots have been generated as PNG files!")

