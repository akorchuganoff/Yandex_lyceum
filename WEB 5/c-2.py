import sys
import os
import pygame
import requests
from webapid3 import lonlat_distance

# python web.http3.py Барнаул Красноармейский 133

toponym_to_find = " ".join(sys.argv[1:])
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}
response = requests.get(geocoder_api_server, params=geocoder_params)
json_response = response.json()
toponym_coodrinates = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]["Point"]["pos"]
x1, y1 = toponym_coodrinates.split()

search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

address_ll = ",".join(toponym_coodrinates.split())

search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": address_ll,
    "type": "biz"}

response = requests.get(search_api_server, params=search_params)
json_response = response.json()

# Получаем первую найденную организацию.
organization = json_response["features"][0]
# Название организации.
org_name = organization["properties"]["CompanyMetaData"]["name"]
# Адрес организации.
org_address = organization["properties"]["CompanyMetaData"]["address"]
# Часы работы
org_hours = organization["properties"]["CompanyMetaData"]["Hours"]["text"]

point = organization["geometry"]["coordinates"]
x2, y2 = point
org_point = "{0},{1}".format(point[0], point[1])

map_params = {
    "l": "map",
    "pt": "{0},pm2dgl~{1},pm2rdm".format(org_point, address_ll)}
map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)
pygame.init()
pygame.display.set_caption('Поиск аптеки 2.0')
screen = pygame.display.set_mode((600, 600))
running = True
screen.fill((255, 255, 255))
screen.blit(pygame.image.load(map_file), (0, 0))
font = pygame.font.Font(None, 30)
adress = font.render(org_address, True, (0, 0, 0))
screen.blit(adress, (0, 460))
name = font.render(org_name, True, (0, 0, 0))
screen.blit(name, (0, 490))
time = font.render(org_hours, True, (0, 0, 0))
screen.blit(time, (0, 520))
distanse = font.render(str(int(lonlat_distance((float(x1), float(y1)),
                                                (float(x2), float(y2))))) + ' метров',
                        True, (0, 0, 0))
screen.blit(distanse, (0, 550))
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
os.remove(map_file)