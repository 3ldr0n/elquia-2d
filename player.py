import pygame

from gamesettings import GameSettings as gs


class Player(pygame.sprite.Sprite):

    def __init__(self, name):
        super().__init__()
        self.width = gs.SCREEN_HEIGHT * (10/100)
        self.height = gs.SCREEN_WIDTH * (10/100)
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((gs.LIGHT_RED))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = gs.SCREEN_HEIGHT - self.height - 30

        self.name = name
        self.hp = 100
        self.maxhp = 100
        self.mp = 100
        self.maxmp = 100
        self.inventory = []
        self.standing = True
        self.jumping = False
        self.velocity = 0

    def is_alive(self):
        return self.hp > 0

    def get_item(self, item):
        self.inventory.append(item)

    def is_on_ground(self):
        """Verifies if the player is on the ground. """
        if self.rect.y == gs.SCREEN_HEIGHT - self.height - 30:
            return True

        return False

    def handle_keys(self):
        """Handles user movement. """
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.rect.x += 5

        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.rect.x -= 5

        if key[pygame.K_SPACE] or key[pygame.K_UP] or key[pygame.K_w]:
            self.standing = False
            self.jumping = True
            self.velocity = 10
            self.rect.y -= self.velocity

        if key[pygame.K_DOWN] or key[pygame.K_s]:
            self.standing = True
            self.jumping = False
            self.velocity = 0
            self.rect.y += 10
