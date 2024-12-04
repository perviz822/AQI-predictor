
from dotenv import load_dotenv
import os
import requests

API_KEY =  os.getenv('API_KEY')

url = f'https://api.weatherbit.io/v2.0/history/airquality?lat=35.5&lon=-78.0&start_date=2024-11-29&end_date=2024-11-30&tz=local&key={API_KEY}'



print(requests.get(url).json())