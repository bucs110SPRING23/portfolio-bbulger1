import requests
import json

class ColormindAPI():
    def __init__(self):
        self.key = "http://colormind.io/api/"

    def return_colors(self):
        r = requests.get(self.key, data='{"model":"default"}')
        response = r.json()
        colors = response.get("result")
        return colors