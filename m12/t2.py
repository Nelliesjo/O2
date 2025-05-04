import requests

import json

kaupunki = input("Minkä kaupungin säätiedot haluat?").capitalize()
pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid=6f2c05652d50ce1b8ddeaeb5c2080c6f&units=metric"

response = requests.get(pyyntö).json()
desc = (response['weather'][0]['description'])
lämpötila = (response['main']['temp'])


print(f"It is currently {lämpötila} degrees Celcius, with {desc} in {kaupunki}.")