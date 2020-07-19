import pygame


class Resource:
    @staticmethod
    def load_image(image_path: str):
        """Load an image and return an image object"""
        try:
            image = pygame.image.load(image_path)

            if image.get_alpha() is None:
                image = image.convert()
            else:
                image = image.convert_alpha()
        except pygame.error as message:
            print("Impossible de charger l'image ", image_path)
            raise SystemExit(message)

        return image, image.get_rect()

    @staticmethod
    def load_image_at(image_path, rect):
        sheet = Resource.load_image(image_path)[0]
        rect = pygame.Rect(rect)
        image = pygame.Surface(rect.size)
        image.blit(sheet, (0, 0), rect)

        return image, image.get_rect()

    @staticmethod
    def get_surface(size, background_color: tuple = None):
        """Returns a surface object according to the defined size and background color"""
        surface = pygame.Surface(size).convert()

        if background_color is not None:
            surface.fill(background_color)

        return surface, surface.get_rect()
