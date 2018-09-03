import os

import pygame

from gamesettings import GameSettings as gs


class Room(pygame.sprite.Sprite):

    def __init__(self, north, south, east, west):
        super().__init__()
        self.north = north
        self.south = south
        self.east = east
        self.west = west
