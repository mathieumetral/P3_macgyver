import pygame

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

    def start(self):
        self.running = True

        while self.running:
            # Make sure the game does not run at more than 60 FPS
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.stop()

            # Update the full display Surface to the screen
            pygame.display.flip()

    def stop(self):
        self.running = False
