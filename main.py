
# http://api.openweathermap.org/geo/1.0/direct?q={city name},
# {state code},{country code}&limit={limit}&appid={API key}
import requests
import os
from dotenv import load_dotenv
from Weather import Weather
load_dotenv()
api_key = os.getenv("API_KEY")
city_name =  input("Enter City Name: ")
state_code = input("Enter State Code: ")
country_code = input("Enter Country Code: ")
q = city_name + ', ' +  state_code + ', ' + country_code


def get_user_location(api_key, q):
    # Define the API endpoint URL
    url = "http://api.openweathermap.org/geo/1.0/direct"
    # Define the parameters
    params = {
        "q": q,
        "limit": 1,
        "appid":  api_key
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        latitude = data[0]["lat"]
        longitude = data[0]["lon"]
        return [latitude, longitude]
            
    else:
        print("Error:", response.status_code)
        return None
location = get_user_location(api_key, q)
def get_user_weather(location, api_key):

    # Define the API endpoint URL
    latitude, longitude = location
    # https://api.openweathermap.org/data/3.0/onecall?
    # lat={lat}&lon={lon}&exclude={part}&appid={API key}
    url = "https://api.openweathermap.org/data/3.0/onecall"
    # Define the parameters
    params = {
    "lat": latitude,
    "lon": longitude,
    "appid":  api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
    # Parse the JSON response
        data = response.json()
        return data
    
    else:
        print("Error:", response.status_code)
# latitude = 40.7128
# longitude =-74.0060
# location = (latitude, longitude)
data = get_user_weather(get_user_location(api_key, q), api_key)
#print(data)
def parse_weather_data(data):
    current_data = data.get("current", {})
    if current_data:
        wind_speed = current_data.get("wind_speed", "N/A")  # Wind speed in meter/sec
        wind_gust = current_data.get("wind_gust", "N/A")  # Wind gust in meter/sec
        cloud_coverage = current_data.get("clouds", "N/A")  # Cloud coverage in percentage
        humidity = current_data.get("humidity", "N/A")  # Humidity in percentage
        pressure = current_data.get("pressure", "N/A")  # Pressure in hPa
        temperature = current_data.get("temp", "N/A")  # Temperature in Kelvin
        precipitation = current_data.get("rain", 0)  # Precipitation in mm
        return wind_speed, wind_gust, cloud_coverage, humidity, pressure, temperature, precipitation
    else:
        return "Weather data not available."
# a = parse_weather_data(data)
# print(parse_weather_data(data))
def create_weather_object(location):
    data = get_user_weather(location, api_key)

    if data:
        wind_speed, wind_gust, cloud_percentage, humidity, pressure, temperature, precipitation = parse_weather_data(data)
        # Create Weather object
    
        weather_obj = Weather(wind_speed, wind_gust, cloud_percentage, humidity, pressure, temperature - 273.15, precipitation)  # Convert temperature from Kelvin to Celsius
        return weather_obj
    else:
        print("Weather data not available.")

weather_obj = create_weather_object(location)

if weather_obj:
    # Print individual elements 
    print("Wind Speed:", weather_obj.wind_speed, "m/s")
    print("Wind Gust:", weather_obj.wind_gust, "m/s")
    print("Cloud Percentage:", weather_obj.cloud_percentage, "%")
    print("Humidity:", weather_obj.humidity, "%")
    print("Pressure:", weather_obj.pressure, "hPa")
    print("Temperature:", weather_obj.temperature, "°C")
    print("Precipitation:", weather_obj.precipitation, "mm")
else:
    print("Weather data not available.")



#current 