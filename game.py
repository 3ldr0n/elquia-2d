import sys

import pygame

from player import Player

pygame.init()
pygame.display.set_caption("Élquia")

SCREEN_SIZE = (500, 500)


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

    def _set_screen(self):
        self.screen.fill((0, 0, 0))

    def run(self):
        clock = pygame.time.Clock()
        player = Player("Eldron")

        while True:
            clock.tick(20)
            self._set_screen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.exit()
                    sys.exit()

            player.draw(self.screen)

            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
