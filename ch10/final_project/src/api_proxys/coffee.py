import requests
import shutil
import urllib3
import json

class Coffee():
    def __init__(self):
        '''
        initialize coffee api
        args: self
        return: none
        '''
        self.key = "https://coffee.alexflipnote.dev/random.json"
        self.http = urllib3.poolmanager.PoolManager(cert_reqs="CERT_NONE")
        self.retry = urllib3.Retry(connect=3, backoff_factor=0.5)

    def image(self):
        '''
        gets new coffee image from api
        args: self
        return: (filepath) filepath for image
        '''
        r = requests.get(self.key)
        j = r.json()
        fileurl = j.get("file")
        filename = "ch10/final_project/assets/image.jpg"
        r = requests.get(fileurl, stream=True)
        openfile = open(filename, "wb")
        shutil.copyfileobj(r.raw, openfile)
        return filename