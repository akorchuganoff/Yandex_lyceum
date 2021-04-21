import requests
import pygame
import os
import sys

map_request = f'http://static-maps.yandex.ru/1.x?l=map&ll=30.076757,59.940481&pl=29.912860,59.891150,30.211311,59.966140,30.239992,59.960115,30.259985,59.958075,30.271579,59.954087,30.288045,59.947912,30.308891,59.945373,30.317809,59.943231&z=10'
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