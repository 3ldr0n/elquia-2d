import pygame

from gamesettings import GameSettings as gs


class TextInput:

    def __init__(self):
        pass

    def draw(self, screen):
        x_mid = gs.SCREEN_WIDTH / 2 - 300
        y_mid_lower = gs.SCREEN_HEIGHT / 2 - 100
        font = pygame.font.SysFont(None, 85)
        text = ""
        pygame.draw.rect(screen, gs.WHITE, (x_mid, y_mid_lower, 300, 100))

    def get_text(self):
        pass
