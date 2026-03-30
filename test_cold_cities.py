from weather_service import WeatherService

# Cold/Low Temperature Cities
cold_cities = {
    # Indian Cold Cities (Himalayan Region)
    'Shimla': 'Himachal Pradesh',
    'Manali': 'Himachal Pradesh',
    'Darjeeling': 'West Bengal',
    'Srinagar': 'Jammu & Kashmir',
    'Nainital': 'Uttarakhand',
    'Mussoorie': 'Uttarakhand',
    'Ooty': 'Tamil Nadu',
    'Coonoor': 'Tamil Nadu',
    'Leh': 'Ladakh',
    'Kufri': 'Himachal Pradesh',
    # International Cold Cities
    'Moscow': 'Russia',
    'Toronto': 'Canada',
    'Stockholm': 'Sweden',
    'Seoul': 'South Korea',
    'Tokyo': 'Japan',
    'New York': 'USA',
    'Berlin': 'Germany',
    'Vienna': 'Austria'
}

print('=' * 90)
print('❄️ COLD & LOW TEMPERATURE CITIES - REAL-TIME WEATHER (March 30, 2026)')
print('=' * 90)
print()

# Indian Cold Cities
print('🇮🇳 INDIA - COLD HILL STATIONS & REGIONS:')
print('-' * 90)
for city in ['Shimla', 'Manali', 'Darjeeling', 'Srinagar', 'Nainital', 'Mussoorie', 'Ooty', 'Coonoor', 'Leh', 'Kufri']:
    result = WeatherService.get_weather_summary(city)
    if result:
        temp = result['temperature']
        humidity = result['humidity']
        precip = result['precipitation']
        status = '❄️' if temp < 15 else '🌤️' if temp < 20 else '🌡️'
        print(f'{status} {city:<15} | Temp: {temp:>5.1f}°C | Humidity: {humidity:>3}% | Precip: {precip:>4.1f}mm')
    else:
        print(f'❌ {city:<15} - Error fetching data')

print()
print('🌍 INTERNATIONAL COLD CITIES:')
print('-' * 90)
for city in ['Moscow', 'Toronto', 'Stockholm', 'Seoul', 'Tokyo', 'New York', 'Berlin', 'Vienna']:
    result = WeatherService.get_weather_summary(city)
    if result:
        temp = result['temperature']
        humidity = result['humidity']
        precip = result['precipitation']
        status = '❄️' if temp < 0 else '🧊' if temp < 10 else '🌤️' if temp < 15 else '🌡️'
        print(f'{status} {city:<15} | Temp: {temp:>5.1f}°C | Humidity: {humidity:>3}% | Precip: {precip:>4.1f}mm')
    else:
        print(f'❌ {city:<15} - Error fetching data')

print()
print('=' * 90)
print('✅ All data from Open-Meteo Real-Time Weather API')
print('=' * 90)
