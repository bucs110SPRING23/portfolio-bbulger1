import requests
import json

class Coffee():
    def __init__(self):
        self.key = "https://github.com/AlexFlipnote/CoffeeAPI/"

    def image(self):
        r = requests.get(self.key)
        print(r.text)

coffee = Coffee()
coffee.image()