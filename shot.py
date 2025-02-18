from circleshape import CircleShape
import pygame
import constants

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, constants.SHOT_RADIUS)
        self.velocity = velocity

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)