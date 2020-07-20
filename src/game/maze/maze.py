import pygame

from config import constants
from src.game.maze.cell import Cell


class Maze:
    def __init__(self, cells_size: tuple,  wall_image, start_image, end_image):
        size = pygame.display.get_window_size()
        self.width, self.height = size[0] // cells_size[0], size[1] // cells_size[1]
        self.grid = [[Cell(x, y, cells_size) for y in range(self.height)] for x in range(self.width)]
        self.wall_image = wall_image
        self.start_image = start_image
        self.end_image = end_image
        self.level_file = None
        self.finish = False

    def generate(self, level_file):
        line_num, row_num = 0, 0

        with open(level_file, "r") as file:
            for line in file:
                row_num = 0
                for char in line:
                    if char == constants.MAZE_WALL_CHARACTER:
                        self.grid[row_num][line_num].create_wall(self.wall_image)
                    elif char == constants.MAZE_START_CHARACTER:
                        self.grid[row_num][line_num].create_start(self.start_image)
                    elif char == constants.MAZE_END_CHARACTER:
                        self.grid[row_num][line_num].create_end(self.end_image)

                    row_num += 1
                line_num += 1

    def draw(self, screen):
        for line in self.grid:
            for cell in line:
                cell.draw(screen)
