import requests
import sys

API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'

cities = input().split(',')
coords = []

for city in cities:
    geocode_request = f'http://geocode-maps.yandex.ru/1.x?geocode={city}&apikey={API_KEY}&format=json'
    response = requests.get(geocode_request)
    if not response:
        print('Ошибка запроса')
        print(f'http code: {response.status_code} {response.reason}')
        sys.exit(-1)
    pos = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
    coords.append((city, list(map(float, pos.split()))))

coords.sort(key=lambda par: par[1][0], reverse=True)
print(coords[0][0])