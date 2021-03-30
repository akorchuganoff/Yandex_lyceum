import sys
import os
import pygame
import requests

# python h-2.py Барнаул Попова 106

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
    "type": "biz",
    "results": "10"}

response = requests.get(search_api_server, params=search_params)
json_response = response.json()


pts = ''

for i in range(10):
    organization = json_response["features"][i]
    org_hours = organization["properties"]["CompanyMetaData"]["Hours"]["text"]

    org_name = organization["properties"]["CompanyMetaData"]["name"]
    # Адрес организации.
    org_address = organization["properties"]["CompanyMetaData"]["address"]


    point = organization["geometry"]["coordinates"]
    x2, y2 = point
    org_point = "{0},{1}".format(point[0], point[1])
    print(org_point)

    if 'круглосуточно' in org_hours:
        pts += f'{org_point},pm2gnm~'
    elif org_hours:
        pts += f'{org_point},pm2blm~'
    else:
        pts += f'{org_point},pm2grm~'

pts = pts[:-1]

print(pts)

map_params = {
    "l": "map",
    "pt": pts
}
map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
print(response.reason)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)
pygame.init()
pygame.display.set_caption('10 аптек')
screen = pygame.display.set_mode((600, 600))
running = True
screen.fill((255, 255, 255))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
os.remove(map_file)
