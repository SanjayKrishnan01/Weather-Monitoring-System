import requests
from django.conf import settings

def get_weather_data(city):
    api_key = settings.OPENWEATHERMAP_API_KEY
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # This will return temperature in Celsius
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return {
            'city': city,
            'main': data['weather'][0]['main'],
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'timestamp': data['dt']
        }
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None