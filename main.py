import requests
import json
from datetime import datetime
import sqlite3

API_URL = "https://api.open-meteo.com/v1/forecast?latitude=-6.4&longitude=106.8186&hourly=temperature_2m&timezone=Asia%2FBangkok&forecast_days=1"
response = requests.get(API_URL).json()
# response = json.dumps(response)

times = response["hourly"]["time"]
times = [int(datetime.strptime(t, "%Y-%m-%dT%H:%M").timestamp()) for t in times]
temperatures = response["hourly"]["temperature_2m"]

temps = []
for i in range(len(times)):
    temps.append((times[i], temperatures[i]))

con = sqlite3.connect("./db/datamart_weather_forecast")
cur = con.cursor()
cur.executemany("insert into forecast values(?, ?)", temps)
con.commit()
con.close()
