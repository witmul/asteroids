import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from bonus import Bonus

class GameState():
    def __init__(self) -> None:
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        self.bonuses = pygame.sprite.Group()

        Player.containers = (self.updatable, self.drawable)
        Asteroid.containers = (self.updatable, self.drawable, self.asteroids)
        AsteroidField.containers = (self.updatable,)
        Shot.containers = (self.updatable, self.drawable, self.shots)
        Bonus.containers = (self.drawable, self.bonuses)

        self.player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
        # temp bonus
        self.bonus = Bonus(200, 234, 20)
        self.asteroid_field = AsteroidField()
        self.active = True
        self.score = 0

    def update(self, dt: float) -> None:
        if not self.active:
            return

        self.updatable.update(dt)
        for asteroid in self.asteroids:
            if asteroid.collide_with(self.player):
                log_event("player_hit")
                self.active = False

            for shot in self.shots:
                if shot.collide_with(asteroid):
                    log_event("asteroid_shot")
                    self.score += 1
                    shot.kill()
                    asteroid.split()

        for bonus in self.bonuses:
            if bonus.collide_with(self.player):
                bonus.activate(self.player)

    def draw(self, screen: pygame.Surface) -> None:
        for item in self.drawable:
            item.draw(screen)
