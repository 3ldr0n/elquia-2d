import os
import sys

import pygame

from enum import Enum

from player import Player
from rooms import OpeningRoom
from gamesettings import GameSettings as gs


class GameStates(Enum):
    START_MENU = 1
    PAUSED = 2
    PLAYING = 3
    INSTRUCTIONS = 4
    ABOUT = 5
    QUIT = 6


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Elzring")
        self.screen = pygame.display.set_mode(gs.SCREEN_SIZE)
        self.state = GameStates.START_MENU
        self.clock = pygame.time.Clock()
        self.FPS = 30

    def _set_screen(self):
        self.screen.fill(gs.BACKGROUND)

    def draw_grid(self):
        for x in range(0, gs.SCREEN_WIDTH, gs.TILESIZE):
            pygame.draw.line(self.screen, gs.LIGHT_GREY,
                             (x, 0), (x, gs.SCREEN_HEIGHT))

        for y in range(0, gs.SCREEN_HEIGHT, gs.TILESIZE):
            pygame.draw.line(self.screen, gs.LIGHT_GREY,
                             (0, y), (gs.SCREEN_WIDTH, y))

    def _draw_menu(self):
        terminus = os.path.join(gs.ASSETS, "fonts/arcadeclassic.ttf")
        font = pygame.font.Font(terminus, 200)
        text = "Elzring"
        text = font.render(text, True, gs.LIGHT_RED)
        x = gs.SCREEN_WIDTH / 2 - text.get_rect().width / 2
        y = gs.SCREEN_HEIGHT / 2 - text.get_rect().height / 2 - 150
        self.screen.blit(text, (x, y))

        x = gs.SCREEN_WIDTH / 2 - gs.TILESIZE*15 / 2
        y = gs.SCREEN_HEIGHT / 2 - gs.TILESIZE*3 / 2
        pygame.draw.rect(self.screen, gs.LIGHT_GREY,
                         (x, y, gs.TILESIZE*15, gs.TILESIZE*3))

    def run(self):
        player = Player()
        characters_sprites = pygame.sprite.Group(player)
        o = OpeningRoom()
        rooms_sprites = pygame.sprite.Group(o)

        while True:
            self.clock.tick(self.FPS)
            self._set_screen()
            self.draw_grid()
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.state == GameStates.START_MENU:
                self._draw_menu()

                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.state = GameStates.PLAYING
            elif self.state == GameStates.PLAYING:
                rooms_sprites.draw(self.screen)
                characters_sprites.draw(self.screen)

                player.handle_keys()
                player.check_border()

            pygame.event.pump()
            pygame.display.flip()
