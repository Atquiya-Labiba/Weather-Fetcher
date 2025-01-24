import requests
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the API key
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL= "http://api.openweathermap.org/data/2.5/weather"

city =input("Enter a city name: ")
requests_url=f"{BASE_URL}?appid={API_KEY}&q={city}"
response=requests.get(requests_url)

if response.status_code==200:
    data=response.json()
    weather=data['weather'][0]["description"]
    print("Weather:",weather)
    temperature=round(data["main"]["temp"]-273.15,2)
    print("Temperature:",temperature, "Celsius")

    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

elif response.status_code == 404:
    print("City not found. Please check the name and try again.")
elif response.status_code == 401:
    print("Invalid API key. Please check your API key.")
else:
    print("An error occured")
