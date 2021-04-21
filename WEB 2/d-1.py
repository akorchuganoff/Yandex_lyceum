import requests
import sys
# 37.622504,55.753215

API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'
coords = input()

geo_request = f'http://geocode-maps.yandex.ru/1.x?geocode={coords}&apikey={API_KEY}&format=json&kind=metro'

response = requests.get(geo_request)
if not response:
    print(f'http code: {response.status_code} ({response.reason})')
    sys.exit(1)


toponym = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
pos = toponym["Point"]["pos"]
address = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["formatted"]

print(f"{address} : {pos}")