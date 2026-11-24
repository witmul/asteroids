import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game_state import GameState
from logger import log_state


def render_score(font: pygame.font.Font, score_value: int, colour: tuple[int, int, int]) -> pygame.Surface:
    return font.render(f"Score: {score_value}", False, colour)

def log_snapshot(screen: pygame.Surface, state: GameState) -> None:
    # log_state() scrapes its caller's local variables, so the groups have to be locals here.
    updatable, drawable, asteroids, shots, bonuses = (
        state.updatable, state.drawable, state.asteroids, state.shots, state.bonuses
    )
    log_state()

def main() -> None:
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)
    state = GameState()

    while True:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r and not state.active:
                # restart the game
                state = GameState()

        state.update(dt)

        screen.fill((0, 0, 0))

        score_text_render = render_score(font, state.score, (255, 255, 255))
        restart_text_render = font.render("To restart press - r", False, (255, 255, 255))

        screen.blit(score_text_render, (SCREEN_WIDTH / 2 - score_text_render.get_width() / 2, 10))

        if state.active:
            log_snapshot(screen, state)
            state.draw(screen)
        else:
            screen.blit(restart_text_render, (SCREEN_WIDTH / 2 - restart_text_render.get_width() / 2, SCREEN_HEIGHT / 2))

        pygame.display.flip()


if __name__ == "__main__":
    main()
