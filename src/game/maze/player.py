import pygame

from src.game.object import Object


class Player(Object):
    def __init__(self, image, size: tuple, grid, tools):
        self.grid = grid
        self.tools_picked = 0
        self.tools = tools
        self.status = 0  # 0 = default, 1 = win, 2 = die

        super().__init__(image, size, True)

    def events(self, event):
        if self.status != 0:
            return

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.move_bottom()
            elif event.key == pygame.K_UP:
                self.move_top()
            elif event.key == pygame.K_RIGHT:
                self.move_right()
            elif event.key == pygame.K_LEFT:
                self.move_left()

    def update(self):
        if not self.is_movable:
            return

        new_position = self.rect.move(self.update_position[0], self.update_position[1])
        if self.area.contains(new_position):
            if self.grid is not None:
                grid_element = self.grid[new_position.x // self.size[0]][new_position.y // self.size[1]]
                if not grid_element.is_wall:
                    self.rect = new_position

                    for tool in self.tools:
                        if self.rect == tool.rect and not tool.hide:
                            self.tools_picked += 1
                            tool.remove()

                if grid_element.is_end:
                    self.status = 1 if self.tools_picked == len(self.tools) else 2
            else:
                self.rect = new_position

        self.update_position = [0, 0]
        pygame.event.pump()  # Internally process pygame event handlers
