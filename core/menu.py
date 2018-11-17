import os
import sys

import pygame

from gamesettings import GameSettings as gs
from gamesettings import GameStates


class Menu:

    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load(
            os.path.join(gs.ASSETS, "images/background.bmp")).convert()
        self.buttons = pygame.image.load(
            os.path.join(gs.ASSETS, "images/botoes.bmp")).convert()
        self.b_width = 372
        self.button_height = 115
        self.gap = 17
        self.button_x_begin = gs.SCREEN_WIDTH / 3
        self.button_x_end = (gs.SCREEN_WIDTH / 3) + self.b_width
        self.menu_mode = True
        self.play_button = None
        self.instructions_button = None
        self.credits_button = None
        self.quit_button = None

    def __set_buttons(self):
        """Crops the buttons """

        self.buttons.set_clip(pygame.Rect(
            0, 0, self.b_width, self.button_height))
        self.play_button = self.buttons.subsurface(self.buttons.get_clip())

        self.buttons.set_clip(pygame.Rect(
            0, self.button_height + self.gap, self.b_width,
            self.button_height))
        self.instructions_button = self.buttons.subsurface(
            self.buttons.get_clip())

        self.buttons.set_clip(pygame.Rect(
            0, 2*(self.button_height + self.gap), self.b_width,
            self.button_height))
        self.credits_button = self.buttons.subsurface(self.buttons.get_clip())

        self.buttons.set_clip(pygame.Rect(
            0, 3*(self.button_height + self.gap), self.b_width,
            self.button_height))
        self.quit_button = self.buttons.subsurface(self.buttons.get_clip())

    def draw_buttons(self):
        """Draw the buttons on screen. """
        self.__set_buttons()
        self.screen.blit(self.play_button,
                         (gs.SCREEN_WIDTH/3, gs.SCREEN_HEIGHT/5))
        self.screen.blit(self.instructions_button,
                         (gs.SCREEN_WIDTH/3, 2*gs.SCREEN_HEIGHT/5))
        self.screen.blit(self.credits_button,
                         (gs.SCREEN_WIDTH/3, 3*gs.SCREEN_HEIGHT/5))
        self.screen.blit(self.quit_button,
                         (gs.SCREEN_WIDTH/3, 4*gs.SCREEN_HEIGHT/5))

    def __mouse_over_play(self, mouse_pos_y):
        """Checks if the mouse is over the play button.

        :param mouse_pos_y: Mouse's y axis position.
        """
        return (mouse_pos_y >= gs.SCREEN_HEIGHT/5 and
                (mouse_pos_y <= gs.SCREEN_HEIGHT/5 +
                 self.button_height))

    def __mouse_over_instructions(self, mouse_pos_y):
        """Checks if the mouse is over the instructions button.

        :param mouse_pos_y: Mouse's y axis position.
        """
        return (mouse_pos_y >= 2*gs.SCREEN_HEIGHT/5 and
                mouse_pos_y <= (2*gs.SCREEN_HEIGHT/5 +
                                self.button_height))

    def __mouse_over_credits(self, mouse_pos_y):
        """Checks if the mouse is over the credits button.

        :param mouse_pos_y: Mouse's y axis position.
        """
        return (mouse_pos_y >= 3*gs.SCREEN_HEIGHT/5 and
                mouse_pos_y <= (3*gs.SCREEN_HEIGHT/5 +
                                self.button_height))

    def __mouse_over_quit(self, mouse_pos_y):
        """Checks if the mouse is over the quit button.

        :param mouse_pos_y: Mouse's y axis position.
        """
        return (mouse_pos_y >= 4*gs.SCREEN_HEIGHT/5 and
                mouse_pos_y <= (4*gs.SCREEN_HEIGHT/5 +
                                self.button_height))

    def run(self, game):
        """Sets the mouse position for buttons and change game state.

        :param game: A game object to change the game state.
        """
        mouse_position = pygame.mouse.get_pos()
        mouse_pos_x = mouse_position[0]
        mouse_pos_y = mouse_position[1]

        if pygame.mouse.get_pressed()[0]:
            if (mouse_pos_x >= self.button_x_begin and
                    mouse_pos_x <= self.button_x_end):
                if self.__mouse_over_play(mouse_pos_y):
                    game.state = GameStates.SET_NAME
                elif self.__mouse_over_instructions(mouse_pos_y):
                    if self.menu_mode:
                        self.menu_mode = False
                        self.background = pygame.image.load(
                            os.path.join(gs.ASSETS,
                                         "images/instrucoes.bmp")).convert()
                elif self.__mouse_over_credits(mouse_pos_y):
                    if self.menu_mode:
                        self.menu_mode = False
                        self.background = pygame.image.load(
                            os.path.join(gs.ASSETS,
                                         "images/creditos.bmp")).convert()
                elif self.__mouse_over_quit(mouse_pos_y):
                    pygame.quit()
                    sys.exit()

            elif not self.menu_mode:
                self.background = pygame.image.load(os.path.join(
                    gs.ASSETS, "images/background.bmp")).convert()
                self.menu_mode = True

        self.draw()

    def draw(self):
        """Draws the background and the buttons. """
        self.screen.blit(self.background, (0, 0))
        if self.menu_mode:
            self.draw_buttons()
