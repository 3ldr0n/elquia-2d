import pygame
import sys
import os

from pygame.locals import *
from gamesettings import GameSettings as gs
from game import GameStates

pygame.init()

# FONTE LUMINARI
TEXT_FONT = pygame.font.SysFont("Luminari", 60)

game_state = GameStates.START_MENU


class Menu:

    running = True

    def __init__(self):
        self.screen = pygame.display.set_mode(gs.SCREEN_SIZE)
        self.background = pygame.image.load('../assets/images/background.bmp')
        self.buttons = pygame.image.load(os.path.join(
            gs.ASSETS, "images/botoes.bmp")).convert_alpha()
        self.counter = 0
        self.menu_items = [
            TEXT_FONT.render("JOGAR", 1, gs.WHITE),
            TEXT_FONT.render("INSTRUCOES", 1, gs.WHITE),
            TEXT_FONT.render("CREDITOS", 1, gs.WHITE),
            TEXT_FONT.render("SAIR", 1, gs.WHITE)
        ]
        self.button_width = 372
        self.button_height = 115
        self.gap_constant = 17
        self.game_state = GameStates.START_MENU

    def set_buttons(self):
        self.buttons.set_clip(pygame.Rect(
            0, 0, self.button_width, self.button_height))
        self.button_play = self.buttons.subsurface(self.buttons.get_clip())

        self.buttons.set_clip(pygame.Rect(
            0, self.button_height + self.gap_constant, self.button_width, self.button_height))
        self.button_instructions = self.buttons.subsurface(
            self.buttons.get_clip())

        self.buttons.set_clip(pygame.Rect(
            0, 2*(self.button_height + self.gap_constant), self.button_width, self.button_height))
        self.button_credits = self.buttons.subsurface(self.buttons.get_clip())

        self.buttons.set_clip(pygame.Rect(
            0, 3*(self.button_height + self.gap_constant), self.button_width, self.button_height))
        self.button_quit = self.buttons.subsurface(self.buttons.get_clip())

        x = gs.SCREEN_WIDTH/2 - self.button_width/2
        self.screen.blit(self.button_play,
                         (x, gs.SCREEN_HEIGHT/5))
        self.screen.blit(self.button_instructions, (x,
                                                    self.gap_constant + self.button_height + gs.SCREEN_HEIGHT/5))
        self.screen.blit(self.button_credits, (x,
                                               2*(self.button_height + 17) + gs.SCREEN_HEIGHT/5))
        self.screen.blit(self.button_quit, (x,
                                            3*(self.button_height + 17) + gs.SCREEN_HEIGHT/5))
        pygame.display.flip()

    def run(self):

        if self.running:
            self.draw()

        mouse_position = pygame.mouse.get_pos()
        mouse_pos_x = mouse_position[0]
        mouse_pos_y = mouse_position[1]

        if pygame.mouse.get_pressed()[0]:
            if self.game_state == GameStates.START_MENU:
                if mouse_pos_x >= (gs.SCREEN_WIDTH/2-self.button_width/2) and mouse_pos_x <= gs.SCREEN_WIDTH + self.button_width:
                    if (mouse_pos_y >= gs.SCREEN_HEIGHT/5
                            and mouse_pos_y <= gs.SCREEN_HEIGHT/5 + self.button_height):
                        self.game_state = GameStates.PLAYING
                    elif (mouse_pos_y >= gs.SCREEN_HEIGHT/5 + self.button_height + self.gap_constant
                          and mouse_pos_y <= self.gap_constant + 2*self.button_height + gs.SCREEN_HEIGHT/5):
                        self.game_state = GameStates.INSTRUCTIONS
                        # CREDITS
                    elif (mouse_pos_y >= 2*(self.button_height+self.gap_constant) + gs.SCREEN_HEIGHT/5
                          and mouse_pos_y <= 3*(self.button_height + self.gap_constant) + gs.SCREEN_HEIGHT/5):
                        self.game_state = GameStates.ABOUT
                        # QUIT
                    elif (mouse_pos_y >= 3*(self.button_height+self.gap_constant) + gs.SCREEN_HEIGHT/5
                          and mouse_pos_y <= 3*(2*self.button_height + 2*self.gap_constant) + gs.SCREEN_HEIGHT/5):
                        pygame.quit()
                        sys.exit()

                    elif self.game_state != GameStates.START_MENU:
                        self.game_stateGameStates.START_MENU
            elif self.game_state == GameStates.INSTRUCTIONS:
                self.set_instructions()
            elif self.game_state == GameStates.ABOUT:
                self.set_about()

        pygame.display.flip()

    def set_instructions(self):
        instructions = pygame.image.load(
            os.path.join(gs.ASSETS, "images/instrucoes.bmp"))
        self.screen.blit(instructions, (0, 0))

    def set_about(self):
        about = pygame.image.load(os.path.join(
            gs.ASSETS, "images/creditos.bmp"))
        self.screen.blit(about, (0, 0))

    def draw(self):

        self.screen.blit(self.background, (0, 0))
        '''
        for i in range(len(self.menu_items)):
            self.screen.blit(self.menu_items[i], (gs.SCREEN_HEIGHT/2, gs.SCREEN_HEIGHT/4 + i * 110))'''

        self.set_buttons()

        pygame.display.flip()


menu = Menu()

while True:
    menu.run()
