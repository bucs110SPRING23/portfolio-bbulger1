import requests
import shutil
import urllib3
import json

class Coffee():
    def __init__(self):
        self.key = "https://coffee.alexflipnote.dev/random.json"
        self.http = urllib3.poolmanager.PoolManager(cert_reqs="CERT_NONE")
        self.retry = urllib3.Retry(connect=3, backoff_factor=0.5)

    def image(self):
        r = requests.get(self.key)
        j = r.json()
        print(r.content)
        fileurl = j.get("file")
        filename = "ch10/final_project/assets/image.jpg"
        print(fileurl)
        r = requests.get(fileurl, stream=True)
        print(r.raw)
        with open(filename, "wb") as f:
            shutil.copyfileobj(r.raw, f)
    
coffee = Coffee()
coffee.image()