import sys

import pygame

from player import Player
from menu import Menu
from rooms import OpeningRoom
from gamesettings import GameSettings as gs
from gamesettings import GameStates


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

    def run(self):
        player = Player()
        characters_sprites = pygame.sprite.Group(player)
        menu = Menu(self.screen)
        opening_room = OpeningRoom()
        opening_room.load_map()
        rooms = {
            "current_room": opening_room
        }

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
                menu.run(self)

                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.state = GameStates.PLAYING
            elif self.state == GameStates.PLAYING:
                rooms["current_room"].render(self.screen)
                characters_sprites.draw(self.screen)

                player.handle_keys()
                player.check_border()

            pygame.event.pump()
            pygame.display.flip()
