import os


class GameSettings:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 500
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

    GROUND_HEIGHT = 30

    LIGHT_RED = (130, 10, 80)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BROWN = (160, 82, 45)
    GREEN = (37.6, 50.2, 22)
    BACKGROUND = BLACK

    ASSETS = os.path.dirname(os.path.abspath(__file__))
    ASSETS = ASSETS.split("core")[0]
    ASSETS = os.path.join(ASSETS, "assets")
