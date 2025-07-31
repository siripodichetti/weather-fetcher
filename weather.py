import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)
data = response.json()

if response.status_code == 200:
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print(f"\nWeather in {city}: {temp}°C, {desc}")
else:
    print("\nError:", data.get("message", "Something went wrong."))

