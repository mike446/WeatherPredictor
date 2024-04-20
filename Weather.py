class Weather: 
  def __init__(self,  wind_speed, wind_gust, cloud_percentage, humidity, pressure, temperature, precipitation):
    self.wind_speed = wind_speed
    self.wind_gust = wind_gust
    self.cloud_percentage = cloud_percentage
    self.humidity = humidity
    self.pressure = pressure
    self.temperature = temperature
    self.precipitation = precipitation
# https://www.kaggle.com/datasets/nelgiriyewithana/global-weather-repository/code
def __str__(self):
        return (
                f"Wind Speed: {self.wind_speed} m/s\n"
                f"Wind Gust: {self.wind_gust} m/s\n"
                f"Cloud Percentage: {self.cloud_percentage}%\n"
                f"Humidity: {self.humidity}%\n"
                f"Pressure: {self.pressure} hPa\n"
                f"Temperature: {self.temperature} °C\n"
                f"Precipitation: {self.precipitation} mm")

weather_data = Weather(wind_speed=5.6, wind_gust=7.2, cloud_percentage=75, humidity=60, pressure=1013, temperature=20, precipitation=0.2)
print(weather_data)