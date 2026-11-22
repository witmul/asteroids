import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_SPEED
from player import Player

class Bonus(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "green", self.position, self.radius, LINE_WIDTH)

    def activate(self, player: "Player")-> None:
        self.kill()
        player.speed *= 2
