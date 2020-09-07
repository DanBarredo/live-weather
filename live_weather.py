import requests
import time


def get_apikey():
    with open("weather-api-key.txt") as api_key:
        key = api_key.read()
    key = key.strip()
    # breakpoint()
    return key


api_key = get_apikey()
country = input("Please enter a country: ")
city = input("Please enter a city: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}"

while True:
    time.sleep(2)
    response = requests.get(url)
    data = response.json()
    print(data['weather'])
