import sys

import pygame

from player import Player
from menu import Menu
from rooms import OpeningBeachRoom
from gamesettings import GameSettings as gs
from gamesettings import GameStates
from textinput import TextInput


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

    def name_input(self, inputs, events):
        """Creates text input dialogue for the name input.

        Parameters
        ----------
        inputs: dict
            Dict of inputs.
        events: list
            Events queue.
        """
        input_name_text = "Qual o seu nome?"
        font = pygame.font.SysFont(None, gs.TILESIZE*5)
        rendered_font = font.render(input_name_text, True, gs.WHITE)
        self.screen.blit(
            rendered_font, (1000 - rendered_font.get_rect().width,
                            0 + rendered_font.get_rect().height))

        if inputs["name_input"].update_text(events):
            self.player.set_name(inputs["name_input"].get_input())
            self.state = GameStates.PLAYING

        inputs["name_input"].draw(self.screen)

    def load_rooms(self):
        opening_beach_room = OpeningBeachRoom()
        opening_beach_room.load_map()
        rooms = {
            "current_room": opening_beach_room,
            "opening_beach_room": opening_beach_room
        }

        return rooms

    def update_sprites(self):
        self.tile_group.update()
        self.characters_sprites.update()
        self.collision_tile_group.update()

    def empty_sprites(self):
        self.tile_group.empty()
        self.collision_tile_group.empty()

    def run(self):
        self.player = Player(self)
        self.characters_sprites = pygame.sprite.Group(self.player)
        menu = Menu(self.screen)
        name_input = TextInput(
            gs.SCREEN_WIDTH // 2 - (gs.TILESIZE * 18) // 2,
            gs.SCREEN_HEIGHT // 2 - (gs.TILESIZE * 4) // 2,
            18, 4)
        inputs = {
            "name_input": name_input
        }
        rooms = self.load_rooms()
        self.tile_group = pygame.sprite.Group()
        self.collision_tile_group = pygame.sprite.Group()

        while True:
            self.clock.tick(self.FPS)
            self._set_screen()
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
                            self.state = GameStates.SET_NAME
            elif self.state == GameStates.SET_NAME:
                self.name_input(inputs, events)
            elif self.state == GameStates.PLAYING:
                rooms["current_room"].render(self, self.player, self.screen)

                self.update_sprites()

                self.tile_group.draw(self.screen)
                self.characters_sprites.draw(self.screen)

                self.player.handle_keys()
                self.player.collide_with_tiles()

                self.empty_sprites()

            pygame.event.pump()
            pygame.display.flip()
