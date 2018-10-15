import pygame
import os
import sys

from pygame.locals import *
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
        self.b_height = 115
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

        self.buttons.set_clip(pygame.Rect(0, 0, self.b_width, self.b_height))
        self.play_button = self.buttons.subsurface(self.buttons.get_clip())

        self.buttons.set_clip(pygame.Rect(
            0, self.b_height + self.gap, self.b_width, self.b_height))
        self.instructions_button = self.buttons.subsurface(
            self.buttons.get_clip())

        self.buttons.set_clip(pygame.Rect(
            0, 2*(self.b_height + self.gap), self.b_width, self.b_height))
        self.credits_button = self.buttons.subsurface(self.buttons.get_clip())

        self.buttons.set_clip(pygame.Rect(
            0, 3*(self.b_height + self.gap), self.b_width, self.b_height))
        self.quit_button = self.buttons.subsurface(self.buttons.get_clip())

    def draw_buttons(self):
        self.__set_buttons()
        self.screen.blit(self.play_button,
                         (gs.SCREEN_WIDTH/3, gs.SCREEN_HEIGHT/5))
        self.screen.blit(self.instructions_button,
                         (gs.SCREEN_WIDTH/3, 2*gs.SCREEN_HEIGHT/5))
        self.screen.blit(self.credits_button,
                         (gs.SCREEN_WIDTH/3, 3*gs.SCREEN_HEIGHT/5))
        self.screen.blit(self.quit_button,
                         (gs.SCREEN_WIDTH/3, 4*gs.SCREEN_HEIGHT/5))

    def run(self, events):
        for event in events:
            mouse_position = pygame.mouse.get_pos()
            mouse_pos_x = mouse_position[0]
            mouse_pos_y = mouse_position[1]

            if pygame.mouse.get_pressed()[0]:
                if (mouse_pos_x >= self.button_x_begin and
                        mouse_pos_x <= self.button_x_end):
                    if (mouse_pos_y >= gs.SCREEN_HEIGHT/5 and
                            mouse_pos_y <= gs.SCREEN_HEIGHT/5 + self.b_height):
                        return GameStates.PLAYING

                    # INSTRUCTIONS BUTTON CLICK
                    elif (mouse_pos_y >= 2*gs.SCREEN_HEIGHT/5 and
                          mouse_pos_y <= 2*gs.SCREEN_HEIGHT/5 + self.b_height):
                        if self.menu_mode:
                            self.menu_mode = False
                            self.background = pygame.image.load(
                                os.path.join(gs.ASSETS,
                                             "images/instrucoes.bmp")).convert()
                    # CREDITS BUTTON CLICK
                    elif (mouse_pos_y >= 3*gs.SCREEN_HEIGHT/5 and
                          mouse_pos_y <= 3*gs.SCREEN_HEIGHT/5 + self.b_height):
                        if self.menu_mode:
                            self.menu_mode = False
                            self.background = pygame.image.load(
                                os.path.join(gs.ASSETS,
                                             "images/creditos.bmp")).convert()
                    # QUIT BUTTON CLICK
                    elif (mouse_pos_y >= 4*gs.SCREEN_HEIGHT/5 and
                          mouse_pos_y <= 4*gs.SCREEN_HEIGHT/5 + self.b_height):
                        pygame.quit()
                        sys.exit()

                elif not self.menu_mode:
                    self.background = pygame.image.load(os.path.join(
                        gs.ASSETS, "images/background.bmp")).convert()
                    self.menu_mode = True

        self.draw()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        if self.menu_mode:
            self.draw_buttons()
