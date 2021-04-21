import requests
import pygame
import os
import sys

API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'

geocode_request = f'http://geocode-maps.yandex.ru/1.x?geocode=Москва&apikey={API_KEY}&format=json'
response = requests.get(geocode_request)
if response:
    coords = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
else:
    sys.exit(1)

coords = ','.join(coords.split())
print(coords)

#Spartak
geocode_request = f'http://geocode-maps.yandex.ru/1.x?geocode=Сокольники стадион&apikey={API_KEY}&format=json'
response = requests.get(geocode_request)
if response:
    coords_spartak = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
else:
    sys.exit(2.1)

coords_spartak = ','.join(coords_spartak.split())

#dinamo
geocode_request = f'http://geocode-maps.yandex.ru/1.x?geocode=Динамо&apikey={API_KEY}&format=json'
response = requests.get(geocode_request)
if response:
    coords_dinamo = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
else:
    sys.exit(2.2)

coords_dinamo = ','.join(coords_dinamo.split())

#luzhniki
geocode_request = f'http://geocode-maps.yandex.ru/1.x?geocode=Лужники&apikey={API_KEY}&format=json'
response = requests.get(geocode_request)
if response:
    coords_luzhniki = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
else:
    sys.exit(2.3)

coords_luzhniki = ','.join(coords_luzhniki.split())


# {долгота},{широта},{стиль}{цвет}{размер}{контент}
print(coords_spartak, coords_dinamo, coords_luzhniki, sep='\n')
map_request = f'http://static-maps.yandex.ru/1.x?l=sat&ll={coords}&pt={coords_spartak},pm2wtm1~{coords_dinamo},pm2wtm2~{coords_luzhniki},pm2wtm3&z=11'
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