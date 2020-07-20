import os
import sys

ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)
IMAGES_DIR = os.path.join(ROOT_DIR, "assets/images")

WIN_TITLE = "Help MacGyver escape"
WIN_BACKGROUND_COLOR = (0, 0, 0)
WIN_ICON = os.path.join(IMAGES_DIR, "logo.png")

MAZE_CELLS_NUMBER = (15, 15)
MAZE_CELLS_SIZE = (40, 40)
MAZE_START_CHARACTER = "s"
MAZE_END_CHARACTER = "e"
MAZE_WALL_CHARACTER = "#"
MAZE_WALL_IMAGE = os.path.join(IMAGES_DIR, "floor.jpg")
MAZE_PLAYER_IMAGE = os.path.join(IMAGES_DIR, "player.png")
MAZE_GUARDIAN_IMAGE = os.path.join(IMAGES_DIR, "guardian.png")
MAZE_TOOLS_NEEDLE_IMAGE = os.path.join(IMAGES_DIR, "needle.png")
MAZE_TOOLS_ETHER_IMAGE = os.path.join(IMAGES_DIR, "ether.png")
MAZE_TOOLS_PLASTIC_TUBE_IMAGE = os.path.join(IMAGES_DIR, "plastic_tube.png")
