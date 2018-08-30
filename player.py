import pygame


class Player:

    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.maxhp = 100
        self.mp = 100
        self.maxmp = 100
        self.inventory = []

    def is_alive(self):
        return self.hp > 0

    def get_item(self, item):
        self.inventory.append(item)

    def draw(self, screen):
        pygame.draw.rect(screen, (230, 10, 0), (0, 0, 50, 100), 4)
