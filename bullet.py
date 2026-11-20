import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH


class Bullet(CircleShape):
    def __init__(self, x: float, y: float, velocity: pygame.Vector2):
        super().__init__(x, y)
        self.velocity = velocity

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
