import sys

import pygame

from player import Player
from gamesettings import GameSettings as gs


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode(gs.SCREEN_SIZE)

    def _set_screen(self):
        self.screen.fill((0, 0, 0))

    def run(self):
        clock = pygame.time.Clock()
        player = Player("Eldron")
        sprites = pygame.sprite.Group(player)

        while True:
            clock.tick(30)
            self._set_screen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            sprites.draw(self.screen)
            player.handle_keys()

            if not player.is_on_ground():
                player.rect.y += 5

            if player.rect.y + player.height > gs.SCREEN_HEIGHT - 30:
                player.rect.y = gs.SCREEN_HEIGHT - player.height - 30

            pygame.display.flip()
