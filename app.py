import requests
from flask import Flask, render_template, request
import geocoder

app = Flask(__name__)

API_KEY = '5b028f8398f16abd556bad3eecdc638b' 

# Function to fetch weather data based on city or coordinates
def get_weather(city=None, lat=None, lon=None):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'appid': API_KEY,
        'units': 'metric',  # For temperature in Celsius
        'q': city,
    }
    
    if lat and lon:  # If latitude and longitude are provided
        params = {
            'appid': API_KEY,
            'units': 'metric',
            'lat': lat,
            'lon': lon
        }
    
    response = requests.get(base_url, params=params)
    return response.json()

# Function to fetch 5-day forecast
def get_forecast(city=None, lat=None, lon=None):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        'appid': API_KEY,
        'units': 'metric',
        'q': city,
    }

    if lat and lon:
        params = {
            'appid': API_KEY,
            'units': 'metric',
            'lat': lat,
            'lon': lon
        }

    response = requests.get(base_url, params=params)
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    forecast_data = None
    location_based = False
    user_city = "City not found"
    
    if request.method == 'POST':
        # Get city from user input
        city = request.form.get('city')
        if city:
            weather_data = get_weather(city=city)
            forecast_data = get_forecast(city=city)
    
    # Check if user wants to get weather based on current location
    if request.method == 'GET' and request.args.get('location_based'):
        g = geocoder.ip('me')  # Get current location coordinates
        if g.latlng:
            lat, lon = g.latlng
            weather_data = get_weather(lat=lat, lon=lon)
            forecast_data = get_forecast(lat=lat, lon=lon)
            location_based = True
    
    return render_template('index.html', weather=weather_data, forecast=forecast_data, location_based=location_based)

if __name__ == '__main__':
    app.run(debug=True)




