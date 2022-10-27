import requests
import json


pyynto = "https://api.chucknorris.io/jokes/random"

try:
    vastaus = requests.get(pyynto)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        print(json_vastaus["value"])
except requests.exceptions.RequestException as e:
    print("Hakua ei voi suorittaa")
