"""
Написать реализацию функции  `get_weather_data(place, api_key=None)`,
в которой необходимо получить данные о погоде
с сайта https://openweathermap.org/.

Функция должна возвращать объект в формате JSON, включающий:
- информацию о названии города (в контексте openweathermap),
- код страны (2 символа),
- широту и долготу, на которой он находится,
- его временной зоне,
- а также о значении температуры (как она ощущается).

Значение временной зоны выводить в формате UTC±N, где N - цифра
временного сдвига. Протестировать выполнение программы со следующими
городами: Чикаго, СПб, Дакка.

Пример вызова функции и получаемого результата.

get_weather_data('Kiev', api_key=key)
{"name": "Kyiv", "coord": {"lon": 30.52, "lat": 50.43},
"country": "UA", "feels_like": 21.96, "timezone": "UTC+3"}


Для организации запросов используйте модуль ```requests```. Для
кодирования и декодирования ```json``` - одноименный модуль.

"""

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
