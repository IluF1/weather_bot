from config import API_KEY
import requests as req



def get_weather(city_for_forecast):
    url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city_for_forecast}'
    response = req.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temperature = data['current']['temp_c']
        
        return temperature
    else:
        return f'Error {response.status_code}'