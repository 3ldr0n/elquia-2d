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


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode(gs.SCREEN_SIZE)
        self.state = GameStates.START_MENU

    def _set_screen(self):
        self.screen.fill(gs.BACKGROUND)

    def _draw_menu(self):
        font = pygame.font.SysFont(None, 100)
        text = "Elzring"
        text = font.render(text, True, gs.LIGHT_RED)
        x = gs.SCREEN_WIDTH / 2 - text.get_rect().width / 2
        y = gs.SCREEN_HEIGHT / 2 - text.get_rect().height / 2 - 150
        self.screen.blit(text, (x, y))

        x = gs.SCREEN_WIDTH / 2 - text.get_rect().width
        pygame.draw.rect(self.screen, gs.LIGHT_GREY,
                         (x, y+150, text.get_rect().width*2, 70))

        mouse_x_pos = pygame.mouse.get_pos()[0]
        mouse_y_pos = pygame.mouse.get_pos()[1]

        if (mouse_x_pos >= x and mouse_x_pos < x+text.get_rect().width*2
                and mouse_y_pos >= y+150 and mouse_y_pos <= y+220):
            if pygame.mouse.get_pressed()[0]:
                self.state = GameStates.PLAYING

    def run(self):
        clock = pygame.time.Clock()
        player = Player("Eldron")
        characters_sprites = pygame.sprite.Group(player)
        room = OpeningRoom()

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
            elif self.state == GameStates.PLAYING:
                room.draw(self.screen)
                characters_sprites.draw(self.screen)
                player.handle_keys()

                if player.rect.x >= gs.SCREEN_WIDTH - 25:
                    player.rect.x = gs.SCREEN_WIDTH - 25

                if player.rect.x <= gs.SCREEN_BORDER:
                    player.rect.x = gs.SCREEN_BORDER

                if player.rect.y <= gs.SCREEN_BORDER:
                    player.rect.y = gs.SCREEN_BORDER

                if player.rect.y + player.height > gs.SCREEN_HEIGHT - gs.SCREEN_BORDER:
                    player.rect.y = gs.SCREEN_HEIGHT - player.height - gs.SCREEN_BORDER

            pygame.event.pump()
            pygame.display.flip()
