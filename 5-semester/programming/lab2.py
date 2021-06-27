import requests
import json


with open('api_key.txt') as f:
    key = f.read()


def get_weather_data(place, api_key=key):
    if api_key is None or place == "":
        return None
    url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s" \
          "&units=metric" % (place, api_key)
    data = requests.get(url).json()
    wrap = {
        "name": data["name"],
        "coord": {"lon": data["coord"]["lon"], "lat": data["coord"]["lat"]},
        "country": data["sys"]["country"],
        "feels_like": round(data["main"]["feels_like"], 2),
        "timezone": "UTC%+d" % int(data["timezone"] / 3600)
    }
    return json.dumps(wrap)


if __name__ == "__lab2__":
    print(get_weather_data("Chicago"))
    print(get_weather_data("Saint Petersburg"))
    print(get_weather_data("Dhaka"))
