import os
import sys

ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)
IMAGES_DIR = os.path.join(ROOT_DIR, "assets/images")

WIN_TITLE = "Help MacGyver escape"
WIN_BACKGROUND_COLOR = (0, 0, 0)
WIN_ICON = os.path.join(IMAGES_DIR, "logo.png")

MAZE_CELLS_NUMBER = (15, 15)
MAZE_CELLS_SIZE = (40, 40)
