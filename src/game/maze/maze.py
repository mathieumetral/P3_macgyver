from random import randint

import pygame

from config import constants
from src.game.maze.cell import Cell
from src.game.maze.player import Player
from src.game.object import Object
from src.utils.resource import Resource


class Maze:
    def __init__(self, cells_size: tuple, player_image, wall_image, start_image, end_image, tools_image):
        size = pygame.display.get_window_size()
        self.width, self.height = size[0] // cells_size[0], size[1] // cells_size[1]
        self.grid = [[Cell(x, y, cells_size) for y in range(self.height)] for x in range(self.width)]
        self.wall_image = wall_image
        self.start_image = start_image
        self.end_image = end_image
        self.level_file = None
        self.finish = False

        self.tools = []
        for tool in tools_image:
            self.tools.append(Object(tool, cells_size))

        self.player = Player(player_image, cells_size, self.grid, self.tools)

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
                        self.player.move_to((row_num, line_num))
                    elif char == constants.MAZE_END_CHARACTER:
                        self.grid[row_num][line_num].create_end(self.end_image)

                    row_num += 1
                line_num += 1

        # Randomly position tools
        for tool in self.tools:
            pos = (randint(0, self.width - 1), randint(0, self.height - 1))
            while self.grid[pos[0]][pos[1]].is_wall:
                pos = (randint(0, self.width - 1), randint(0, self.height - 1))

            tool.move_to(pos)

    def draw(self, screen):
        for line in self.grid:
            for cell in line:
                cell.draw(screen)

        for tool in self.tools:
            tool.draw(screen)

    def events(self, event):
        self.player.events(event)

    def display_screen(self, screen):
        if self.player.status == 0 or self.finish:
            return

        font = pygame.font.SysFont('Comic Sans MS', 30)
        title = font.render('You win!' if self.player.status == 1 else 'You lose!', False, (255, 255, 255))
        size = title.get_size()
        menu = Resource.get_surface((size[0] + 20, size[1] + 20), (0, 0, 0))[0]
        menu_rect = menu.get_rect(center=screen.get_rect().center)

        menu.blit(title, (10, 10))

        screen.blit(menu, menu_rect)
        self.finish = True
