import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        ran_angle = random.uniform(20,50)
        trajectory_1 = self.velocity.rotate(ran_angle)
        trajectory_2 = self.velocity.rotate(-ran_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        break_1 = Asteroid(self.position.x, self.position.y, new_radius)
        break_2 = Asteroid(self.position.x, self.position.y, new_radius)
        break_1.velocity = trajectory_1 * 1.2
        break_2.velocity = trajectory_2 * 1.2
