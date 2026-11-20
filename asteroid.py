import pygame
import random

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            # Define vectors for the asteroid movement
            # before defining new asteroids
            asteroit_one_vector = self.velocity.rotate(angle)
            asteroit_two_vector = self.velocity.rotate(-angle)
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_one = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_one.velocity = asteroit_one_vector * 1.2
            asteroid_two = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_two.velocity = asteroit_two_vector * 1.2
