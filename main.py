import pygame
import requests
import sys
import os


def load_map():
    map_request = "https://static-maps.yandex.ru/1.x/?ll=37.620070,55.753630&spn=0.005,0.005&l=map"
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        sys.exit()
    map_file_name = "map.png"
    with open(map_file_name, "wb") as file:
        file.write(response.content)
    return map_file_name


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    while True:
        map_file = load_map()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os.remove(map_file)
                sys.exit()
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
