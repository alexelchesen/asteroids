import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    print(f"Starting Asteroids!\n"\
    f"Screen width: {SCREEN_WIDTH}\n"\
    f"Screen height: {SCREEN_HEIGHT}\n")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()

    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateables, drawables)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    Asteroid.containers = (updateables, drawables, asteroids)
    AsteroidField.containers = (updateables)
    asteroid_field = AsteroidField()

    Shot.containers = (updateables, drawables, shots)

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateables.update(dt)

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over! You collided with an asteroid!")
                return

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
                    break



        screen.fill((0, 0, 0)) # fill the screen with black

        for sprite in drawables:
            sprite.draw(screen)

        pygame.display.flip()

        dt = fps.tick(120) / 1000.0



if __name__ == "__main__":
    main()
