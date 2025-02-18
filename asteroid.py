from circleshape import CircleShape
import constants
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        
        super().__init__(x, y, radius)
           
    def draw(self, surface):
        pygame.draw.circle(surface, (0, 255, 0), self.position.xy, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)

            new_vector1 = self.velocity.rotate(angle)
            new_vector2 = self.velocity.rotate(-angle)

            new_vector1 *= 1.2
            new_vector2 *= 1.2

            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid1.velocity = new_vector1
            asteroid2.velocity = new_vector2
        