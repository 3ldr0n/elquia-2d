import pygame

from gamesettings import GameSettings as gs


class TextInput(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        """Inputs any kind of text on screen.

        Parameters ---------- x: int
            X axis position of the input bar.
        y: int
            Y axis position of the input bar.
        width: int
            Width of the input bar. Its value is multiplied by the size of
            the tile.
        height: int
            Height of the input bar. Its value is multiplied by the size of
            the tile.
        """
        self.x = x
        self.y = y
        self.width = width * gs.TILESIZE
        self.height = height * gs.TILESIZE
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font = pygame.font.SysFont(None, self.height//2)
        self.text = ""

    def update_text(self, events):
        """Updates text on key press.

        Parameters
        ----------
        events: list
            Events queue.

        Returns
        -------
        return_press: bool
            Return key indicates the user finished the input.
        """
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
        """Draws the input bar and the text.

        Parameters
        ----------
        screen: pygame.Surface
            Screen object.
        """
        pygame.draw.rect(screen, gs.WHITE, self.rect)
        rendered = self.font.render(self.text, True, gs.LIGHT_RED)
        screen.blit(rendered, (self.x, (self.y) +
                               rendered.get_rect().height))

    def get_input(self):
        """Returns the text attribute. """
        return self.text
