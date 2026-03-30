from weather_service import WeatherService

# Major North Indian Cities
north_cities = {
    'Delhi': 'National Capital',
    'Jaipur': 'Pink City, Rajasthan',
    'Lucknow': 'Uttar Pradesh',
    'Kanpur': 'Uttar Pradesh',
    'Chandigarh': 'Union Territory',
    'Amritsar': 'Punjab',
    'Ludhiana': 'Punjab',
    'Indore': 'Madhya Pradesh',
    'Gwalior': 'Madhya Pradesh',
    'Bhopal': 'Madhya Pradesh',
    'Agra': 'Uttar Pradesh',
    'Varanasi': 'Uttar Pradesh',
    'Meerut': 'Uttar Pradesh',
    'Mathura': 'Uttar Pradesh',
    'Udaipur': 'Rajasthan'
}

print('=' * 80)
print('🇮🇳 NORTH INDIAN CITIES - REAL-TIME WEATHER (March 30, 2026)')
print('=' * 80)
print()

for city, region in north_cities.items():
    result = WeatherService.get_weather_summary(city)
    if result:
        print(f'📍 {city:<15} ({region:<25})')
        print(f'   Temperature: {result["temperature"]}°C  |  Humidity: {result["humidity"]}%  |  Precipitation: {result["precipitation"]}mm')
        print()
    else:
        print(f'❌ {city:<15} - Error fetching data')
        print()

print('=' * 80)
print('✅ All data from Open-Meteo Real-Time Weather API')
print('=' * 80)
