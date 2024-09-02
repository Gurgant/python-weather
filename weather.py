from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Milan"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={
        os.getenv("API_KEY")}&q={city}&units=metric'

    try:
        weather_data = requests.get(request_url).json()
        return weather_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***\n")
    city = input("\nEnter city name: ")

    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = "Milan"

    weather_data = get_current_weather(city)
    print("\nCurrent weather data for", city)
    pprint(weather_data)


# def get_current_weather(city="Milan"):
#     url = "https://api.openweathermap.org/data/2.5/weather"
#     querystring = {
#         "q": city,
#         "appid": os.getenv("OPENWEATHERMAP_API_KEY"),
#         "units": "metric"
#     }
#     response = requests.get(url, params=querystring)
#     return response.json()
