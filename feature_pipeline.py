import requests

import time
from datetime import datetime, timedelta
import csv

from tqdm import tqdm
from dotenv import load_dotenv
import os



load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')

LAT = 40.3777
LON = 49.8920
#latitude and longitude of baku

END_DATE = datetime.now()
START_DATE =  datetime(2022,1,13)


def fetch_daily_data(date):
    params = {
        "lat":LAT,
        "lon":LON,
        "key":API_KEY,
        "start_date":date.strftime("%Y-%m-%d"),
        "end_date":(date+timedelta(days=1)).strftime("%Y-%m-%d"),
        "tz":"local"
        
    }
    response =  requests.get(BASE_URL,params=params)
    if response.status_code ==200:
        return response.json()
    else:
        print(f"Error fething the data for {date.strftime("%Y-%m-%d")}")

csv_file = "baku_air_quality_data.csv"        
csv_headers = ["timestamp", "aqi", "o3", "so2", "no2", "co", "pm25", "pm10"]     
total_days = (END_DATE - START_DATE).days + 1

   
with open(csv_file,"w",newline = "") as file:
    writer = csv.writer(file)  
    writer.writerow(csv_headers) 
    pbar = tqdm(total=total_days, desc="Fetching data", unit="day")
    current_date = START_DATE
    while current_date <= END_DATE:
        daily_data = fetch_daily_data(current_date)
        if daily_data and 'data' in daily_data:
                for hour_data in daily_data['data']:
                    row = [
                        hour_data['timestamp_local'],
                        hour_data['aqi'],
                        hour_data['o3'],
                        hour_data['so2'],
                        hour_data['no2'],
                        hour_data['co'],
                        hour_data['pm25'],
                        hour_data['pm10']
                    ]
                    writer.writerow(row)
        current_date += timedelta(days=1)
        pbar.update(1) 
        time.sleep(1)
        
print(f"Data saved to {csv_file}")        

    
        
