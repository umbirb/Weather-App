from pip._vendor import requests
import json

#api key
api_key = '9fdb1db98ab73a584bad6247d0207310'
#input city name
location = input('Enter the city name: ')
 # API endpoint for current weather
current_weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
# API endpoint for 5-day forecast   
print(current_weather_url)\
# Make a GET request to the current weather API
response = requests.get(current_weather_url)
# Convert the response to JSON
weather_data = response.json()

# Extract the temperature, humidity, and wind speed from thesyd JSON object
temperature = weather_data['main']['temp']
humidity = weather_data['main']['humidity']
wind_speed = weather_data['wind']['speed']
# Print the temperature, humidity, and wind speed
print(f'Temperature: {temperature}°C')
print(f'Humidity: {humidity}%')
print(f'Wind speed: {wind_speed} m/s')
#store the data in a dictionary
request_one_weather_data = {
    'temperature': temperature,
    'humidity': humidity,
    'wind_speed': wind_speed
}
#ask user if they want to make another request, veiw previous data, show forcast for city/country or exit
while True:
    user_input = input('Enter 1 to make another request, 2 to view previous data, 3 to view 5-day forecast, or 4 to exit: ')
    if user_input == '1':
        location = input('Enter the city name: ')
        current_weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
        response = requests.get(current_weather_url)
        weather_data = response.json()
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        print(f'Temperature: {temperature}°C')
        print(f'Humidity: {humidity}%')
        print(f'Wind speed: {wind_speed} m/s')
        request_one_weather_data = {
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed
        }
    elif user_input == '2':
        print(request_one_weather_data)
    elif user_input == '3':
        location = input('Enter the city name: ')
        forecast_weather_url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric'
        response = requests.get(forecast_weather_url)
        forecast_data = response.json()
        for i in range(0, 40, 8):
            temperature = forecast_data['list'][i]['main']['temp']
            humidity = forecast_data['list'][i]['main']['humidity']
            wind_speed = forecast_data['list'][i]['wind']['speed']
            print(f'Temperature: {temperature}°C')
            print(f'Humidity: {humidity}%')
            print(f'Wind speed: {wind_speed} m/s')
    elif user_input == '4':
        exit()
    else:
        print('Invalid input')
        continue
