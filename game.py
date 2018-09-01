import sys

import pygame

from player import Player
from gamesettings import GameSettings as gs


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode(gs.SCREEN_SIZE)

    def _set_screen(self):
        self.screen.fill(gs.BACKGROUND)

    def _draw_ground(self):
        ground = pygame.rect.Rect(
            (0, gs.SCREEN_HEIGHT-30, gs.SCREEN_WIDTH, 30))
        pygame.draw.rect(self.screen, gs.BROWN, ground)

        grass = pygame.rect.Rect((0, gs.SCREEN_HEIGHT-30, gs.SCREEN_WIDTH, 8))
        pygame.draw.rect(self.screen, gs.GREEN, grass)

    def run(self):
        clock = pygame.time.Clock()
        player = Player("Eldron")
        sprites = pygame.sprite.Group(player)

        while True:
            clock.tick(20)
            self._set_screen()
            self._draw_ground()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            sprites.draw(self.screen)
            player.handle_keys()

            if not player.is_on_ground():
                player.rect.y += 5
                player.set_falling_image()
            else:
                player.set_idle_image(player.rect.x, player.rect.y)

            player.set_walking_image()

            if player.rect.y + player.height > gs.SCREEN_HEIGHT - 30:
                player.rect.y = gs.SCREEN_HEIGHT - player.height - 30

            pygame.display.flip()
