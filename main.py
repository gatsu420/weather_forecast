import requests
import json

API_URL = 'https://api.open-meteo.com/v1/forecast?latitude=-6.4&longitude=106.8186&hourly=temperature_2m&timezone=Asia%2FBangkok&forecast_days=1'
response = requests.get(API_URL).json()
# response = json.dumps(response)

times = response['hourly']['time']
temperatures = response['hourly']['temperature_2m']
temps = dict(zip(times, temperatures))

print(temps)
