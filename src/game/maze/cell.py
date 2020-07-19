from src.game.object import Object
from src.utils.resource import Resource


class Cell(Object):
    def __init__(self, x: int, y: int, size: tuple):
        self.size = size
        self.image, self.rect = Resource.get_surface(self.size, (0, 0, 0))

        super().__init__((self.image, self.rect), self.size)

        self.rect.x = x * self.size[0]
        self.rect.y = y * self.size[1]

        self.x = x
        self.y = y

        self.is_wall = False
        self.is_start = False
        self.is_end = False

    def _create_element(self, element_type: int, image):
        self.is_wall = True if element_type == 1 else False
        self.is_start = True if element_type == 2 else False
        self.is_end = True if element_type == 3 else False
        self.image = image[0]
        self._update_image_size()

    def create_wall(self, image):
        self._create_element(1, image)

    def create_start(self, image):
        self._create_element(2, image)

    def create_end(self, image):
        self._create_element(3, image)
