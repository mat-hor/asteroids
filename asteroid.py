from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)

        vector_1 = pygame.Vector2.rotate(self.velocity, random_angle)
        vector_2 = pygame.Vector2.rotate(self.velocity, -random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        split_asteroid_1 = Asteroid(self.position[0],self.position[1], new_radius)
        split_asteroid_2 = Asteroid(self.position[0],self.position[1], new_radius)

        split_asteroid_1.velocity = vector_1 * 1.2
        split_asteroid_2.velocity = vector_2
        
