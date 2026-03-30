import requests
from datetime import datetime
import json

class WeatherService:
    """Fetch weather data and provide climate-based recommendations"""
    
    # Using Open-Meteo API (free, no API key required)
    OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"
    GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
    
    @staticmethod
    def get_coordinates(location_name):
        """Convert location name to latitude and longitude"""
        try:
            params = {
                "name": location_name,
                "count": 1,
                "language": "en",
                "format": "json"
            }
            response = requests.get(WeatherService.GEOCODING_URL, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            
            if 'results' in data and len(data['results']) > 0:
                result = data['results'][0]
                return {
                    'latitude': result['latitude'],
                    'longitude': result['longitude'],
                    'name': result.get('name', location_name),
                    'country': result.get('country', ''),
                    'timezone': result.get('timezone', 'UTC')
                }
            return None
        except Exception as e:
            print(f"Error in geocoding: {e}")
            return None
    
    @staticmethod
    def get_current_weather(latitude, longitude):
        """Fetch current weather data for given coordinates"""
        try:
            params = {
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,relative_humidity_2m,precipitation,weather_code",
                "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,weather_code",
                "timezone": "auto"
            }
            response = requests.get(WeatherService.OPEN_METEO_URL, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            return data
        except Exception as e:
            print(f"Error fetching weather: {e}")
            return None
    
    @staticmethod
    def get_weather_summary(location_name):
        """Get weather summary for a location"""
        coords = WeatherService.get_coordinates(location_name)
        if not coords:
            return None
        
        weather_data = WeatherService.get_current_weather(coords['latitude'], coords['longitude'])
        if not weather_data:
            return None
        
        current = weather_data.get('current', {})
        
        return {
            'location': coords['name'],
            'country': coords['country'],
            'latitude': coords['latitude'],
            'longitude': coords['longitude'],
            'temperature': round(current.get('temperature_2m', 0), 1),
            'humidity': current.get('relative_humidity_2m', 0),
            'precipitation': current.get('precipitation', 0),
            'raw_data': weather_data
        }

def classify_climate_zone(temp, humidity, precipitation):
    """Classify climate zone based on temperature, humidity, and precipitation"""
    if temp < 10:
        return "cold"
    elif 10 <= temp < 20:
        return "temperate"
    elif 20 <= temp < 25:
        return "subtropical"
    else:
        return "tropical"

def get_rainfall_type(precipitation):
    """Classify rainfall level"""
    if precipitation < 50:
        return "low"
    elif 50 <= precipitation < 200:
        return "moderate"
    else:
        return "high"
