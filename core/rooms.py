import os

from enum import Enum

import pygame

from gamesettings import GameSettings as gs


class Rooms(Enum):
    OPENING_ROOM = 0
    SECONDING_ROOM = 1


class Room(pygame.sprite.Sprite):

    def __init__(self, north, south, east, west, _id):
        super().__init__()
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.room_map = []
        self._id = _id


class OpeningRoom(Room):

    def __init__(self):
        super().__init__(Rooms.SECONDING_ROOM, Rooms.SECONDING_ROOM,
                         Rooms.SECONDING_ROOM, Rooms.SECONDING_ROOM,
                         Rooms.OPENING_ROOM)
        self.image = pygame.image.load(os.path.join(gs.MAP, "opening.png"))
        self.rect = self.image.get_rect()


class SecondingRoom(Room):

    def __init__(self):
        super().__init__(Rooms.OPENING_ROOM, Rooms.OPENING_ROOM,
                         Rooms.OPENING_ROOM, Rooms.OPENING_ROOM,
                         Rooms.SECONDING_ROOM)
        self.image = pygame.image.load(os.path.join(gs.MAP, "seconding.png"))
        self.rect = self.image.get_rect()
