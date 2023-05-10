import requests
import json

class ColormindAPI():
    def __init__(self):
        '''
        initialize colormind api proxy
        args: self
        return: none
        '''
        self.key = "http://colormind.io/api/"

    def return_colors(self):
        '''
        gets new color pallete from api
        args: self
        return: (list) colors
        '''
        r = requests.get(self.key, data='{"model":"default"}')
        response = r.json()
        colors = response.get("result")
        return colors