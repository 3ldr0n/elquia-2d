import pygame

from gamesettings import GameSettings as gs


class TextInput(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.font = pygame.font.SysFont(None, self.height//2)
        self.text = ""

    def update_text(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    return False
                else:
                    self.text += event.unicode
                    return False

    def draw(self, screen):
        pygame.draw.rect(screen, gs.WHITE, self.rect)
        rendered = self.font.render(self.text, True, gs.LIGHT_RED)
        print(rendered.get_rect().height)
        screen.blit(rendered, (self.x//2, (self.y // 2) +
                               rendered.get_rect().height))

    def get_input(self):
        return self.text
