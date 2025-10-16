import requests

api_key = '2b7bc619685af934d31083818594d669'

user_input = input('Enter the city name: ')

weather_data = requests.get(
    f'https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}'
    )

data = weather_data.json()

if data.get('cod') != 200:
        print('\nCity not found')
        print(f'No such city: {user_input}')

else:
    # Access all values from the same data object
        city = data['name']
        weather = data['weather'][0]['main']
        temp = data['main']['temp']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        wind_speed = data['wind']['speed']
        wind_deg = data['wind']['deg']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        condition = data['weather'][0]['description']
        country = data['sys']['country']

# Details that a user will see
def details():
    print(f'\nWeather Details of {city.title()}')
    print('\nWEATHER:')
    print(f'Weather today in {city.title()} is {weather.title()}')
    print('\nTEMPERATURE:')
    print(f'Current temperature: {temp}°F')
    print(f'Maximum temperature: {temp_max}°F')
    print(f'Minimum temperature: {temp_min}°F')
    print('\nOTHER DETAILS:')
    print(f'Current pressure: {pressure} hPa')
    print(f'Current humidity: {humidity}%')
    print(f'Current wind speed: {wind_speed} km/h')

details()

# ____________________________________THE-END____________________________________
# Created by: Izram khan
# Date: 16-Oct-2025
