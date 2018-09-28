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

        self.screen.blit(self.button_play,
                         (gs.SCREEN_HEIGHT/2, gs.SCREEN_WIDTH/5))
        self.screen.blit(self.button_instructions, (gs.SCREEN_HEIGHT/2,
                                                    self.gap_constant + self.button_height + gs.SCREEN_WIDTH/5))
        self.screen.blit(self.button_credits, (gs.SCREEN_HEIGHT/2,
                                               2*(self.button_height + 17) + gs.SCREEN_WIDTH/5))
        self.screen.blit(self.button_quit, (gs.SCREEN_HEIGHT/2,
                                            3*(self.button_height + 17) + gs.SCREEN_WIDTH/5))
        pygame.display.flip()

    def run(self):

        if self.running:
            self.draw()

        mouse_position = pygame.mouse.get_pos()
        mouse_pos_x = mouse_position[0]
        mouse_pos_y = mouse_position[1]

        
        if pygame.mouse.get_pressed()[0]:
            print("clickou lek")
            if mouse_pos_x >= gs.SCREEN_WIDTH/2 and mouse_pos_x <= gs.SCREEN_WIDTH + self.button_width:
                # PLAY
                if mouse_pos_y >= gs.SCREEN_HEIGHT/5 and mouse_pos_y <= gs.SCREEN_HEIGHT + self.button_height:
                    game_state = GameStates.PLAYING
                    print("JOGANDO")
                # INSTRUCTIONS
                elif mouse_pos_y >= gs.SCREEN_HEIGHT/5 and mouse_pos_y <= self.gap_constant + self.button_height + gs.SCREEN_WIDTH/5:
                    game_state = GameStates.INSTRUCTIONS
                    print("INSTRUCOES")
                # CREDITS
                elif mouse_pos_y >= 2*(self.button_height+self.gap_constant) + gs.SCREEN_HEIGHT/5 and mouse_pos_y <= 2*(self.button_height + 17) + gs.SCREEN_WIDTH/5:
                    game_state = GameStates.ABOUT
                    print("CREDITOS")
                # QUIT
                elif mouse_pos_y >= 3*(self.button_height+self.gap_constant) + gs.SCREEN_HEIGHT/5 and mouse_pos_y <= 3*(self.button_height + 17) + gs.SCREEN_WIDTH/5:
                    game_state = GameStates.QUIT
                    print("SAIR")

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                elif event.key == pygame.K_UP:
                    if self.counter > 0:
                        self.counter -= 1
                elif event.key == pygame.K_DOWN:
                    if self.counter < 3:
                        self.counter += 1

                elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:

                    # ENTER THE GAME
                    if self.counter == 0:
                        self.running = False
                        game_state = GameStates.PLAYING
                        # CALL GAME FUNCTION  game.run() ?????

                    # ENTER THE INSTRUCTIONS SCREEN
                    elif self.counter == 1:
                        game_state = GameStates.INSTRUCTIONS
                        # CALL INSTRUCTIONS FUNCTION

                    # ENTER THE CREDITS SCREEN
                    elif self.counter == 2:
                        game_state = GameStates.ABOUT
                        # CALL ABOUT FUNCTION

                    # QUIT
                    elif self.counter == 3:
                        self.running = False

    def draw(self):

        self.screen.blit(self.background, (0, 0))
        '''
        for i in range(len(self.menu_items)):
            self.screen.blit(self.menu_items[i], (gs.SCREEN_HEIGHT/2, gs.SCREEN_HEIGHT/4 + i * 110))'''

        self.set_buttons()

        pygame.display.flip()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
                        pygame.display.quit()


menu = Menu()

menu.run()
