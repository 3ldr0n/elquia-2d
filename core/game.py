import sys

import pygame

from enum import Enum

from background import Background
from player import Player
from gamesettings import GameSettings as gs


class GameStates(Enum):
    START_MENU = 1
    PAUSED = 2
    PLAYING = 3


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode(gs.SCREEN_SIZE)
        self.state = GameStates.START_MENU

    def _set_screen(self):
        self.screen.fill(gs.BACKGROUND)

    def _draw_menu(self):
        font = pygame.font.SysFont(None, 100)
        text = "Federação de élquia"
        text = font.render(text, True, gs.LIGHT_RED)
        x = gs.SCREEN_WIDTH / 2 - text.get_rect().width / 2
        y = gs.SCREEN_HEIGHT / 2 - text.get_rect().height / 2 - 100
        self.screen.blit(text, (x, y))

    def run(self):
        clock = pygame.time.Clock()
        player = Player("Eldron")
        characters_sprites = pygame.sprite.Group(player)

        while True:
            clock.tick(20)
            self._set_screen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.state == GameStates.START_MENU:
                self._draw_menu()
                key = pygame.key.get_pressed()

                if key[pygame.K_RETURN]:
                    self.state = GameStates.PLAYING
            else:
                characters_sprites.draw(self.screen)
                player.handle_keys()

                if player.rect.y + player.height > gs.SCREEN_HEIGHT:
                    player.rect.y = gs.SCREEN_HEIGHT - player.height

            pygame.event.pump()
            pygame.display.flip()
