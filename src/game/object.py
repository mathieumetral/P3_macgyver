import pygame


class Object(pygame.sprite.Sprite):
    def __init__(self, image, size: tuple, is_movable: bool = False):
        super().__init__()

        self.image = image[0]
        self.size = size
        self._update_image_size()
        self.rect = self.image.get_rect()
        self.hide = False

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.is_movable = is_movable
        self.update_position = [0, 0]

    def _update_image_size(self):
        self.image = pygame.transform.scale(self.image, self.size)

    def update(self):
        if not self.is_movable:
            return

        new_position = self.rect.move(self.update_position[0], self.update_position[1])
        if self.area.contains(new_position):
            self.rect = new_position

        self.update_position = [0, 0]
        pygame.event.pump()  # Internally process pygame event handlers

    def move_right(self):
        self.update_position[0] += self.size[0]

    def move_left(self):
        self.update_position[0] -= self.size[0]

    def move_top(self):
        self.update_position[1] -= self.size[1]

    def move_bottom(self):
        self.update_position[1] += self.size[1]

    def move_to(self, new_position: tuple):
        self.rect.x = new_position[0] * self.size[0]
        self.rect.y = new_position[1] * self.size[1]

    def draw(self, screen):
        screen.blit(self.image, self.rect)
