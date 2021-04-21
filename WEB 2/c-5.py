import requests
import pygame
import os
import sys

API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'

geocode_request = f'http://geocode-maps.yandex.ru/1.x?geocode=Австралия&apikey={API_KEY}&format=json'
response = requests.get(geocode_request)
if response:
    coords = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
else:
    sys.exit(1)

coords = ','.join(coords.split())
print(coords)

map_request = f'http://static-maps.yandex.ru/1.x?l=sat&ll={coords}&size=600,450&z=4'
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(2)

map_file = 'map.png'
with open(map_file, 'wb') as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

os.remove(map_file)