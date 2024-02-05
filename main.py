import os
import sys

import pygame
import requests

zxc = 10
running = True

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
def req():
    map_request = f"https://static-maps.yandex.ru/1.x/?ll=43.462467,56.248144&z={zxc % 21}&l=map"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запишем полученное изображение в файл.
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
req()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                zxc += 1
                req()
            if event.key == pygame.K_DOWN:
                zxc -= 1
                req()
pygame.quit()
