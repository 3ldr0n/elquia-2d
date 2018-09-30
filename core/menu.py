import pygame
import os
import sys

from pygame.locals import *
from gamesettings import GameSettings as gs

pygame.init()

class Menu:

    def __init__(self):
        self.screen = pygame.display.set_mode(gs.SCREEN_SIZE)
        pygame.display.set_caption("UM JOGO MTO FODA!")
        self.background = pygame.image.load('../assets/images/background.bmp').convert()
        self.buttons = pygame.image.load("../assets/images/botoes.bmp").convert()
        self.b_width = 372
        self.b_height = 115
        self.gap = 17
        self.button_x_begin = (gs.SCREEN_WIDTH/3)
        self.button_x_end = (gs.SCREEN_WIDTH/3)+(self.b_width)

    def set_buttons(self):

        #CROPPING PLAY BUTTON)
        self.buttons.set_clip(pygame.Rect(0, 0, self.b_width, self.b_height))
        self.play_button = self.buttons.subsurface(self.buttons.get_clip())
        #CROPPING INSTRUCTIONS BUTTON
        self.buttons.set_clip(pygame.Rect(0, self.b_height + self.gap, self.b_width, self.b_height))
        self.instructions_button = self.buttons.subsurface(self.buttons.get_clip())
        #CROPPING CREDITS BUTTON
        self.buttons.set_clip(pygame.Rect(0, 2*(self.b_height + self.gap), self.b_width, self.b_height))
        self.credits_button = self.buttons.subsurface(self.buttons.get_clip())
        #CROPPING QUIT BUTTON
        self.buttons.set_clip(pygame.Rect(0, 3*(self.b_height + self.gap), self.b_width, self.b_height))
        self.quit_button = self.buttons.subsurface(self.buttons.get_clip())
        
        #PRINTING PLAY BUTTON
        self.screen.blit(self.play_button, (gs.SCREEN_WIDTH/3,gs.SCREEN_HEIGHT/5))
        #PRINTING INSTRUCTIONS BUTTON
        self.screen.blit(self.instructions_button, (gs.SCREEN_WIDTH/3,2*gs.SCREEN_HEIGHT/5))
        #PRINTING CREDITS BUTTON
        self.screen.blit(self.credits_button, (gs.SCREEN_WIDTH/3,3*gs.SCREEN_HEIGHT/5))
        #PRINTING QUIT BUTTON
        self.screen.blit(self.quit_button, (gs.SCREEN_WIDTH/3,4*gs.SCREEN_HEIGHT/5))


    def run(self):
        
        running = True
        while running:    
            for event in pygame.event.get():
                mouse_position = pygame.mouse.get_pos()
                mouse_pos_x = mouse_position[0]
                mouse_pos_y = mouse_position[1]
                
                if pygame.mouse.get_pressed()[0]:
                    if(mouse_pos_x >= self.button_x_begin and mouse_pos_x <= self.button_x_end):
                        # PLAY BUTTON CLICK
                        if mouse_pos_y >= gs.SCREEN_HEIGHT/5 and mouse_pos_y <= gs.SCREEN_HEIGHT/5 + self.b_height:
                            print("JOGAR")
                            print(mouse_position)
                        # INSTRUCTIONS BUTTON CLICK
                        elif mouse_pos_y >= 2*gs.SCREEN_HEIGHT/5 and mouse_pos_y <= 2*gs.SCREEN_HEIGHT/5 + self.b_height:
                            print("INSTRUCOES")
                            print(mouse_position)
                        # CREDITS BUTTON CLICK
                        elif mouse_pos_y >= 3*gs.SCREEN_HEIGHT/5 and mouse_pos_y <= 3*gs.SCREEN_HEIGHT/5 + self.b_height:
                            print("CREDITOS")
                            print(mouse_position)
                        # QUIT BUTTON CLICK
                        elif mouse_pos_y >= 4*gs.SCREEN_HEIGHT/5 and mouse_pos_y <= 4*gs.SCREEN_HEIGHT/5 + self.b_height:
                            print("SAIR")
                            print(mouse_position)

                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        print("AE KRALHO")


            self.draw()

    
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.set_buttons()
        pygame.display.flip()
        


menu = Menu()

while True:
    menu.run()

