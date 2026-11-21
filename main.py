import pygame
import sys

from logger import log_state, log_event
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    score = pygame.font.SysFont(None, 36)
    dt = 0.0
    score_value = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:

        score_render = score.render(f"Score: {score_value}", False, "white")
        dt = clock.tick(60) / 1000
        log_state()
        
        screen.fill((0, 0, 0))
        screen.blit(score_render, (SCREEN_WIDTH / 2 - score_render.get_width() / 2, 10))

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collide_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collide_with(asteroid):
                    log_event("asteroid_shot")
                    score_value += 1
                    shot.kill()
                    asteroid.split()

        for item in drawable:
            item.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()




if __name__ == "__main__":
    main()
