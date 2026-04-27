from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

# Using Open-Meteo API (free, no API key required)
WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"
GEOCODING_API_URL = "https://geocoding-api.open-meteo.com/v1/search"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/weather', methods=['GET'])
def get_weather():
    latitude = request.args.get('latitude', type=float)
    longitude = request.args.get('longitude', type=float)
    
    if not latitude or not longitude:
        return jsonify({'error': 'Latitude and longitude required'}), 400
    
    try:
        params = {
            'latitude': latitude,
            'longitude': longitude,
            'current': 'temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m',
            'hourly': 'temperature_2m,weather_code',
            'daily': 'weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum',
            'timezone': 'auto'
        }
        
        response = requests.get(WEATHER_API_URL, params=params)
        response.raise_for_status()
        
        data = response.json()
        return jsonify(data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/search-location', methods=['GET'])
def search_location():
    query = request.args.get('query', '')
    
    if not query:
        return jsonify({'error': 'Query required'}), 400
    
    try:
        params = {
            'name': query,
            'count': 10,
            'language': 'en',
            'format': 'json'
        }
        
        response = requests.get(GEOCODING_API_URL, params=params)
        response.raise_for_status()
        
        return jsonify(response.json())
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
