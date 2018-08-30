import sys

import pygame

from player import Player
from gamesettings import GameSettings as gs

pygame.init()
pygame.display.set_caption("Élquia")


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
            clock.tick(20)
            self._set_screen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            sprites.draw(self.screen)
            player.handle_keys()

            pygame.display.flip()
