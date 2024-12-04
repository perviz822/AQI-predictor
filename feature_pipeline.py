import requests
import time
from datetime import datetime, timedelta
import csv
import sys

from tqdm import tqdm
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API configurations
API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')
print(BASE_URL)

# Coordinates for Baku
LAT = 40.3777
LON = 49.8920

# Date range for data fetching
END_DATE = datetime.now()
START_DATE = datetime(2024, 12, 2)

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
        
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        return response.json()
    
    except requests.RequestException as e:
        print(f"Error fetching data for {date.strftime('%Y-%m-%d')}: {e}")
        return None

def main():
    # CSV file configuration
    csv_file = "baku_air_quality_data.csv"        
    csv_headers = ["timestamp", "aqi", "o3", "so2", "no2", "co", "pm25", "pm10"]     
    total_days = (END_DATE - START_DATE).days + 1

    try:
        with open(csv_file, "a", newline='', encoding='utf-8') as file:
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
                        print("the row")
                        writer.writerow(row)
                        print('the row was written')
                
                current_date += timedelta(days=1)
                pbar.update(1) 

            
            pbar.close()
        
        print(f"Data saved to {csv_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()