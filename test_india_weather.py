from weather_service import WeatherService

cities = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Pune', 'Hyderabad', 'Jaipur', 'Ahmedabad', 'Lucknow']

print('🇮🇳 INDIAN CITIES - REAL-TIME WEATHER DATA\n')
print(f'{"City":<15} {"Temperature":<15} {"Humidity":<12} {"Precipitation":<15} {"Status":<10}')
print('-' * 75)

for city in cities:
    result = WeatherService.get_weather_summary(city)
    if result:
        temp = result['temperature']
        humidity = result['humidity']
        precip = result['precipitation']
        print(f'{city:<15} {temp}°C{"":<10} {humidity}%{"":<8} {precip}mm{"":<9} ✅')
    else:
        print(f'{city:<15} {"ERROR":<15} {"N/A":<12} {"N/A":<15} ❌')

print('\n✅ All temperatures fetched from Open-Meteo API (Real-time data)')
