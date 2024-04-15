
# http://api.openweathermap.org/geo/1.0/direct?q={city name},
# {state code},{country code}&limit={limit}&appid={API key}
import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
city_name =  input("Enter City Name: ")
state_code = input("Enter State Code: ")
country_code = input("Enter Country Code: ")
q = city_name + ', ' +  state_code + ', ' + country_code
import requests

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
        return "Error:" + response.status_code
# latitude = 40.7128
# longitude =-74.0060
# location = (latitude, longitude)
data = (get_user_location(api_key, q), api_key)
def parse_weather_data(data): 
    if 'current' in data and 'weather' in data['current']:
        return data['current']['weather'][0]['description']
    else:
        return "Weather data not available."

weather_state = parse_weather_data(data)
print("Todays Weather Status: " + weather_state)