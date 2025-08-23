from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.height_multiplier = random.uniform(0.5, 1.5)

    def draw(self, screen):
        #pygame.draw.circle(screen, color = "white", center = self.position, radius = self.radius, width = 2)
        pygame.draw.ellipse(screen, color = "white", rect = pygame.Rect(self.position.x - self.radius, self.position.y - self.height_multiplier * self.radius, 2 * self.radius, 2 * self.height_multiplier * self.radius), width = 1)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < 2 * ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        direction1 = self.velocity.rotate(angle)
        direction2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = direction1 * 1.2
        asteroid2.velocity = direction2 * 1.2