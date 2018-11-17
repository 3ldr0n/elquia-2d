import os

from enum import Enum

import pygame

from gamesettings import GameSettings as gs
from tiles import Sand, Ocean, Rock, Trail, Grass


class Rooms(Enum):
    OPENING_BEACH_ROOM = 0
    FOLLOWING_BEACH_ROOM = 1


class Room(pygame.sprite.Sprite):

    def __init__(self, north, south, east, west, _id):
        super().__init__()
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.room_map = []
        self._id = _id
        self.player_enter = False

    def load_map(self):
        pass

    def render(self, game, player, screen):
        pass


class OpeningBeachRoom(Room):

    def __init__(self):
        super().__init__(Rooms.FOLLOWING_BEACH_ROOM,
                         Rooms.FOLLOWING_BEACH_ROOM,
                         Rooms.FOLLOWING_BEACH_ROOM,
                         Rooms.FOLLOWING_BEACH_ROOM,
                         Rooms.OPENING_BEACH_ROOM)

    def load_map(self):
        map_file = os.path.join(gs.MAP, "opening_beach.txt")
        with open(map_file, "r") as room:
            for line in room:
                self.room_map.append(line)

    def render(self, game, player, screen):
        passage = False
        for y, line in enumerate(self.room_map):
            for x, column in enumerate(line):
                if x == 0 or y == 0:
                    passage = True
                else:
                    passage = False

                if column == "S":
                    Sand(game, x, y, passage)
                elif column == "O":
                    Ocean(game, x, y)
                elif column == "R":
                    Rock(game, x, y)
                elif column == "T":
                    Trail(game, x, y, passage)
                elif column == "P":
                    Sand(game, x, y, passage)
                    if self.player_enter is False:
                        player.rect.x = x * gs.TILESIZE
                        player.rect.y = y * gs.TILESIZE
                        self.player_enter = True


class FollowingBeach(Room):

    def __init__(self):
        super().__init__(Rooms.OPENING_BEACH_ROOM, Rooms.OPENING_BEACH_ROOM,
                         Rooms.OPENING_BEACH_ROOM, Rooms.OPENING_BEACH_ROOM,
                         Rooms.FOLLOWING_BEACH_ROOM)

    def load_map(self):
        map_file = os.path.join(gs.MAP, "following_beach.txt")
        with open(map_file, "r") as room:
            for line in room:
                self.room_map.append(line)

    def render(self, game, player, screen):
        passage = False
        for y, line in enumerate(self.room_map):
            for x, column in enumerate(line):
                if x == 32 or y == 32:
                    passage = True
                else:
                    passage = False

                if column == "S":
                    Sand(game, x, y, passage)
                elif column == "O":
                    Ocean(game, x, y)
                elif column == "R":
                    Rock(game, x, y)
                elif column == "T":
                    Trail(game, x, y, passage)
                elif column == "G":
                    Grass(game, x, y, passage)
                elif column == "P":
                    Trail(game, x, y, passage)
                    if self.player_enter is False:
                        player.rect.x = x * gs.TILESIZE
                        player.rect.y = y * gs.TILESIZE
                        self.player_enter = True
