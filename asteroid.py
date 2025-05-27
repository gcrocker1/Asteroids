from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

# Class for asteroids
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()     # built in pygame method to delete object and remove it from groups--if asteroid is big enough, we'll spawn others below

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rand_angle = random.uniform(20, 50)
        rand_vec_1 = self.velocity.rotate(rand_angle)
        rand_vec_2 = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        aster_1 = Asteroid(self.position[0], self.position[1], new_radius)
        aster_2 = Asteroid(self.position[0], self.position[1], new_radius)
        aster_1.velocity = rand_vec_1 * 1.2     # Make the new asteroids faster
        aster_2.velocity = rand_vec_2 * 1.2
        
