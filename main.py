import pygame, requests, sys, os


def load_map():
    map_request = "https://static-maps.yandex.ru/1.x/?ll=37.620070,55.753630&spn=0.005,0.005&l=map"
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        sys.exit()
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            break
        map_file = load_map()
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
    pygame.quit()
    os.remove(map_file)