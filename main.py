import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids!\n"\
        f"Screen width: {SCREEN_WIDTH}\n"\
        f"Screen height: {SCREEN_HEIGHT}\n")
    while True:
        screen.fill((0, 0, 0)) # fill the screen with black
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()
