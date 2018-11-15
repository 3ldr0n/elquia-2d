import os

from enum import Enum


class GameSettings:
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 768
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
    SCREEN_BORDER = 0
    TILESIZE = 32
    GRID_WIDTH = SCREEN_WIDTH / TILESIZE
    GRID_HEIGHT = SCREEN_HEIGHT / TILESIZE

    # Aliases
    BORDER = SCREEN_BORDER
    WIDTH = SCREEN_WIDTH
    HEIGHT = SCREEN_HEIGHT

    LIGHT_RED = (130, 10, 80)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BROWN = (160, 82, 45)
    GREEN = (37.6, 50.2, 22)
    LIGHT_GREY = (128, 128, 128)
    BACKGROUND = BLACK
    SAND_YELLOW = (237, 201, 175)
    OCEAN_BLUE = (79, 66, 181)

    BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
    BASE_FOLDER = BASE_FOLDER.split("core")[0]
    ASSETS = os.path.join(BASE_FOLDER, "assets")
    MAP = os.path.join(BASE_FOLDER, "map")


class GameStates(Enum):
    START_MENU = 1
    PAUSED = 2
    PLAYING = 3
    INSTRUCTIONS = 4
    CREDITS = 5
    QUIT = 6
    SET_NAME = 7
