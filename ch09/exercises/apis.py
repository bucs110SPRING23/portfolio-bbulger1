import requests

def main():
    city = input("Enter city: ")
    r = requests.get("http://api.waqi.info/feed/" + city + "/?token=7d49949fa4f42b68951234c6d044fd9923bbb07a")
    city_data = r.json()
    aqi = city_data['data']['aqi']
    print("Air Quality Index:", aqi)

main()