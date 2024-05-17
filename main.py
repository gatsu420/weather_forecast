import requests
from datetime import datetime
from utils.db import SQLite
from utils.writer import FileWriter

def get_forecast(url):
    r = requests.get(url).json()

    return r

def main():
    response = get_forecast("https://api.open-meteo.com/v1/forecast?latitude=-6.4&longitude=106.8186&hourly=temperature_2m&timezone=Asia%2FBangkok&forecast_days=1")

    times = response["hourly"]["time"]
    times = [int(datetime.strptime(t, "%Y-%m-%dT%H:%M").timestamp()) for t in times]
    temperatures = response["hourly"]["temperature_2m"]

    temps = []
    for i in range(len(times)):
        temps.append((times[i], temperatures[i]))

    curtime = datetime.now().timestamp()
    for temp in temps:
        if temp[0] >= curtime:
            tidy_time = datetime.fromtimestamp(temp[0]).strftime("%Y-%m-%d %H:%M")
            info = f"Next forecast: {temp[1]} on {tidy_time}" 
            
            w = FileWriter()
            w.append("runtime.txt", info)
            print(info)

            break

    db_writer = SQLite()
    db_writer.executemany(
        "./db/datamart_weather_forecast",
        "insert into forecast values(?, ?)",
        temps
        )

if __name__ == "__main__":
    main()
