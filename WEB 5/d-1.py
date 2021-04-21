import requests
import sys
from random import randrange
import pygame
import os

# python d-1.py

cities = ["Лиссабон", "Лондон", "Лос-Анджелес", "Нью-Йорк", "Питер", "Барнаул"]


def draw():
    global cities

    toponym_to_find = cities[randrange(0, len(cities))]
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

    map_params = {
        "l": "map",
        "ll": ",".join([x1, y1]),
        "spn": '0.005,0.005'
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    with open(map_file, "wb") as file:
        file.write(response.content)
    return


map_file = 'map.png'
draw()

pygame.init()
pygame.display.set_caption('Поиск аптеки 2.0')
screen = pygame.display.set_mode((600, 600))
running = True
screen.fill((255, 255, 255))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw()
    screen.fill((255, 255, 255))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
pygame.quit()
os.remove(map_file)
