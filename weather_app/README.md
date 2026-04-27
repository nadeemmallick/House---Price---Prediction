# Weather Dashboard

## Features
✅ Real-time weather data from Open-Meteo API (free, no API key needed)
✅ Location search with autocomplete
✅ Current weather conditions
✅ Hourly forecast (24 hours)
✅ 7-day forecast
✅ Geolocation support
✅ Responsive design
✅ Beautiful UI with gradient background

## Installation

### 1. Prerequisites
- Python 3.7+
- pip (Python package manager)

### 2. Clone and Setup
```bash
git clone https://github.com/nadeemmallick/House---Price---Prediction.git
cd weather_app
```

### 3. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Application
```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

## API Used
**Open-Meteo API** - Free weather API (no authentication required)
- Current weather
- Hourly forecast (168 hours)
- Daily forecast (7 days)
- Geocoding for location search

## Project Structure
```
weather_app/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── templates/
    └── index.html        # Frontend HTML/CSS/JS
```

## API Endpoints

### Get Weather
`GET /api/weather?latitude=40.7128&longitude=-74.0060`

Response includes:
- Current conditions (temperature, humidity, wind speed)
- Hourly forecast (168 hours)
- Daily forecast (7 days with max/min temps)
- Timezone information

### Search Location
`GET /api/search-location?query=London`

Response includes:
- Location names
- Latitude/Longitude coordinates
- Admin regions
- Countries

## Deployment Options

### Heroku
```bash
heroku create your-app-name
git push heroku weather-dashboard:main
```

### PythonAnywhere
1. Upload files to PythonAnywhere
2. Create web app and configure
3. Point to app.py

### Docker
Create `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "app:app"]
```

## Features Explained

### Geolocation
- On first load, requests user's location permission
- Falls back to New York if denied

### Location Search
- Autocomplete suggestions as you type
- Debounced API calls (300ms delay)
- Click suggestions or press Enter to search

### Weather Display
- Current temperature, humidity, wind speed
- 24-hour hourly forecast with temperatures
- 7-day forecast with highs/lows and precipitation

### Responsive Design
- Works on desktop, tablet, and mobile
- Gradient background with smooth animations
- Hover effects on cards

## Customization

- Change colors in `index.html` (CSS gradient section)
- Modify forecast days in JavaScript
- Add more weather parameters from Open-Meteo API
- Customize temperature units (Celsius/Fahrenheit)

## Weather Codes Reference

The dashboard includes a complete mapping of WMO weather codes to descriptions:
- 0: Clear sky
- 1-3: Various cloud conditions
- 45-48: Fog
- 51-82: Precipitation (drizzle, rain, snow, showers)
- 85-86: Snow showers
- 95-99: Thunderstorms

## Troubleshooting

### Port 5000 Already in Use
```bash
python app.py --port 5001
```

### Geolocation Not Working
- Check browser permissions
- Ensure HTTPS (or localhost)
- Allow location access

### API Errors
- Check internet connection
- Verify coordinates are valid
- Check Open-Meteo API status

## License
MIT License

## Author
Nadeem Mallick
