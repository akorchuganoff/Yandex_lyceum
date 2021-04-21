import math
import requests
import sys

def lonlat_distance(a, b):

    degree_to_meters_factor = 111 * 1000 # 111 километров в метрах
    a_lon, a_lat = a
    b_lon, b_lat = b

    # Берем среднюю по широте точку и считаем коэффициент для нее.
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)

    # Вычисляем смещения в метрах по вертикали и горизонтали.
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    # Вычисляем расстояние между точками.
    distance = math.sqrt(dx * dx + dy * dy)

    return distance

address = input()
API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'

geo_request = f'http://geocode-maps.yandex.ru/1.x?geocode=Останкинская телебашня&apikey={API_KEY}&format=json'
response = requests.get(geo_request)
if not response:
    sys.exit(1)
firstCoords = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
firstCoords = list(map(float, firstCoords.split()))

geo_request = f'http://geocode-maps.yandex.ru/1.x?geocode={address}&apikey={API_KEY}&format=json'
response = requests.get(geo_request)
if not response:
    sys.exit(2)
secondCoords = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
secondCoords = list(map(float, secondCoords.split()))


L = lonlat_distance(firstCoords, secondCoords)/1000
print(f'рассторяние в километрах: {L}')
h = max(0, (L / 3.6 - math.sqrt(525))) ** 2
print(f'Высота антены приемника: {h}')