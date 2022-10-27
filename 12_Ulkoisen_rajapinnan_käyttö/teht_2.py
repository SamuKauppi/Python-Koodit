import requests
import json


def make_a_request(pyynto):
    try:
        vastaus = requests.get(pyynto)
        if vastaus.status_code == 200:
            json_vastaus = vastaus.json()
            return json_vastaus
    except requests.exceptions.RequestException as e:
        return ""


def search_country(target, key):
    search_request = f"https://api.openweathermap.org/geo/1.0/direct?q={target}&limit=1&appid={key}"
    return_value = make_a_request(search_request)
    return return_value


def search_weather(lat, lon, key):
    request = f"https://api.openweathermap.org/data/2.5/weather?lat={str(lat)}&lon={str(lon)}&appid={key}&units=metric"
    return_value = make_a_request(request)
    return return_value


place = input("Syötä paikkakunnan nimi: ")

API_key = "bf045cfc3c3e9ae9ee15ae3bbb0faf63"
value = search_country(place, API_key)
weather = search_weather(value[0]["lat"], value[0]["lon"], API_key)
temp = weather["main"]["temp"]
print(f"{temp} Celcius")


