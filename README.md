# WeatherPredictor
Currently, the proposed experiments to test the effectiveness of the AI are simple. Once the AI has cleared through testing data, it will be introduced to new weather data that it has not been exposed to before. This will be done in two ways. The first way will be using data from older forecasts, and seeing if the AI’s prediction will match the actual weather from the record. The second way will be for it to receive data from a recent forecast and see if it will be able to predict up to a certain time in the future.

5-Hour Intervals: We can use the data from the last 24 hours to make Predictions updated every 5 hours offer a compromise between frequency and granularity, providing useful forecasts for medium-term planning and decision-making. This timing may be suitable for users who need periodic updates but can accommodate slightly longer intervals between forecasts.

Weather Parameters?  
- Wind speed(metre/sec)
- Wind gust (metre/sec)
- Current clouds (cloud percentage)
- Humidity
- Pressure
- Temperature
- precipitation



Weather Parameters(Input)
- Location(Latitude and Longitude)
- Idea: User can input an address and we can convert that to latitude and longitude(Google Maps Geocoding API)??


Weather Output
- We can define prompts based on output for example: 
 Expect a day of partly cloudy with rain
  

Checklist
- first commit(test)
