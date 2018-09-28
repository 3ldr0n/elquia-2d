import pygame
import sys

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
        self.background = pygame.image.load('../images/background.bmp')
        self.counter = 0
        self.menu_items = [
            TEXT_FONT.render("JOGAR", 1, gs.WHITE),
            TEXT_FONT.render("INSTRUCOES", 1, gs.WHITE),
            TEXT_FONT.render("CREDITOS", 1, gs.WHITE),
            TEXT_FONT.render("SAIR", 1, gs.WHITE)
        ]

    def run(self):

        if self.running:
            self.draw()
            
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
        
        for i in range(len(self.menu_items)):
            self.screen.blit(self.menu_items[i], (gs.SCREEN_HEIGHT/2, gs.SCREEN_HEIGHT/4 + i * 110))

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
