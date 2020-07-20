import pygame

from config import constants
from src.game.maze.maze import Maze
from src.utils.resource import Resource


class MacGyverGame:
    def __init__(self, title: str, background_color: tuple, cells_number: tuple, cells_size: tuple, icon: str = None):
        # Display window initialization
        pygame.init()
        self.screen = pygame.display.set_mode((cells_number[0] * cells_size[0], cells_number[1] * cells_size[1]))
        pygame.display.set_caption(title)
        pygame.font.init()

        if icon is not None:
            pygame.display.set_icon(Resource.load_image(icon)[0])

        self.background = Resource.get_surface(self.screen.get_size(), background_color)[0]  # Fill the background
        self.clock = pygame.time.Clock()  # Clock initialization
        self.running = False

        self.maze = Maze(
            cells_size,
            Resource.load_image(constants.MAZE_PLAYER_IMAGE),
            Resource.load_image_at(constants.MAZE_WALL_IMAGE, (39, 0, cells_size[0], cells_size[1])),
            Resource.load_image_at(constants.MAZE_WALL_IMAGE, (319, 39, cells_size[0], cells_size[1])),
            Resource.load_image(constants.MAZE_GUARDIAN_IMAGE),
            [
                Resource.load_image(constants.MAZE_TOOLS_NEEDLE_IMAGE),
                Resource.load_image(constants.MAZE_TOOLS_ETHER_IMAGE),
                Resource.load_image(constants.MAZE_TOOLS_PLASTIC_TUBE_IMAGE)
            ]
        )

        # RenderPlain allows you to manage multiple Sprite objects
        self.player_sprite = pygame.sprite.RenderPlain(self.maze.player)
        self.tools_sprite = pygame.sprite.RenderPlain(self.maze.tools)

    def draw(self):
        self.maze.generate("assets/levels/1")  # Load level 1
        self.maze.draw(self.background)
        self.screen.blit(self.background, (0, 0))

        pygame.display.flip()  # Update the Surface

    def start(self):
        self.running = True
        self.draw()

        while self.running:
            # Make sure the game does not run at more than 60 FPS
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.stop()

                self.maze.events(event)

            self.screen.blit(self.background, self.maze.player.rect, self.maze.player.rect)

            self.player_sprite.update()  # Call the update method of every member sprite
            self.tools_sprite.draw(self.screen)
            self.player_sprite.draw(self.screen)

            # Update the full display Surface to the screen
            pygame.display.flip()

    def stop(self):
        self.running = False
