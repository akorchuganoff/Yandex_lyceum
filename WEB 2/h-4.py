import requests
import sys
import pygame
import os

API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'

geo_request = f'http://geocode-maps.yandex.ru/1.x?geocode=Барнаул&apikey={API_KEY}&format=json'
response = requests.get(geo_request)

if response:
    pos_barnaul = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
else:
    sys.exit(1)

geo_request = f'http://geocode-maps.yandex.ru/1.x?geocode=Москва&apikey={API_KEY}&format=json'
response = requests.get(geo_request)

if response:
    pos_moscow = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
else:
    sys.exit(2)

geo_request = f'http://geocode-maps.yandex.ru/1.x?geocode=Санкт-Петербург&apikey={API_KEY}&format=json'
response = requests.get(geo_request)

if response:
    pos_spb = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
else:
    sys.exit(3)

pos_barnaul = ','.join(pos_barnaul.split())
pos_moscow = ','.join(pos_moscow.split())
pos_spb = ','.join(pos_spb.split())

print(pos_barnaul, pos_moscow, pos_spb)




map_request = f'http://static-maps.yandex.ru/1.x?l=map&ll={pos_barnaul}&z=10'
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(2)

map_file = 'map_brn.png'
with open(map_file, 'wb') as file:
    file.write(response.content)


map_request = f'http://static-maps.yandex.ru/1.x?l=map&ll={pos_moscow}&z=10'
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(2)

map_file = 'map_msk.png'
with open(map_file, 'wb') as file:
    file.write(response.content)


map_request = f'http://static-maps.yandex.ru/1.x?l=map&ll={pos_spb}&z=10'
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(2)

map_file = 'map_spb.png'
with open(map_file, 'wb') as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
running = True
count = 0

d = {0: 'map_brn.png',
     1: 'map_msk.png',
     2: 'map_spb.png'}

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                count -= 1
            if event.key == pygame.K_RIGHT:
                count += 1

    screen.blit(pygame.image.load(d[count % 3]), (0, 0))
    pygame.display.flip()
pygame.quit()

os.remove('map_brn.png')
os.remove('map_msk.png')
os.remove('map_spb.png')