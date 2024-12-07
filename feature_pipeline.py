import requests
import time
from datetime import datetime, timedelta
import csv
import sys

from tqdm import tqdm

import os
import pandas as pd


# Load environment variables#

# Get API configurations
API_KEY = os.environ.get('API_KEY')
print(API_KEY)


# Coordinates for Baku
LAT = 40.3777
LON = 49.8920

# Date range for data fetching



df = pd.read_csv('baku_aqi.csv')
date_values =  df['timestamp'].values
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
last_timestamp = df['timestamp'].iloc[-1]





END_DATE = datetime(2023,4,15)
START_DATE =last_timestamp

def fetch_daily_data(date):
    """
    Fetch air quality data for a specific date
    
    Args:
        date (datetime): Date to fetch data for
    
    Returns:
        dict or None: JSON response or None if error
    """
    try:
        params = {
            "lat": LAT,
            "lon": LON,
            "key": API_KEY,
            "start_date": date.strftime('%Y-%m-%d'),
            "end_date": (date + timedelta(days=1)).strftime('%Y-%m-%d'),
            "tz": "local"
        }
        
        response = requests.get('https://api.weatherbit.io/v2.0/history/airquality/', params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        return response.json()
    
    except requests.RequestException as e:
        print(f"Error fetching data for {date.strftime('%Y-%m-%d')}: {e}")
        return None

def main():
   # 2024-12-03T20:00:00
    # CSV file configuration
    csv_file = "baku_aqi.csv"        
    csv_headers = ["timestamp", "aqi", "o3", "so2", "no2", "co", "pm25", "pm10"] 
    print(START_DATE)    
    total_days = (END_DATE - START_DATE).days + 1
    print(total_days)
    

    try:
        
        with open(csv_file,'a',newline='') as file:
            writer = csv.writer(file)  
            pbar = tqdm(total=total_days, desc="Fetching data", unit="day")
            current_date = START_DATE
            
            while current_date <= END_DATE:
                daily_data = fetch_daily_data(current_date)
                
                if daily_data and 'data' in daily_data:
                    for hour_data in daily_data['data']:
                        row = [
                            hour_data.get('timestamp_local', ''),
                            hour_data.get('aqi', ''),
                            hour_data.get('o3', ''),
                            hour_data.get('so2', ''),
                            hour_data.get('no2', ''),
                            hour_data.get('co', ''),
                            hour_data.get('pm25', ''),
                            hour_data.get('pm10', '')
                        ]
                        print(row)
                        
                        if row[0] not in date_values:
                         writer.writerow(row)
                        
                        print('the row was written')
                
                current_date += timedelta(days=1)
                pbar.update(1) 

            
            pbar.close()
            file.close()
        
        print(f"Data saved to {csv_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 




    
    