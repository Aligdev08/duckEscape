import pygame
from typing import Tuple
import random


class Duck:
    __dir = "Ducks/duck.png"
    speed: float = 1

    def __init__(self, position: Tuple[int, int], scale: float = 0.3):
        self.scale = scale
        self.pos = position
        self.duck_surface = self._initialize()
        self.caught = False
        self.type = None  # default
        self.direction = (random.choice([5, -5]), random.choice([5, -5]))

    def _initialize(self) -> pygame.Surface:
        duck = pygame.image.load(self.__dir).convert_alpha()
        scaled_size = (int(duck.get_width() * self.scale), int(duck.get_height() * self.scale))
        return pygame.transform.scale(duck, scaled_size)

    def is_caught(self) -> bool:
        return self.caught

    def get_pos(self) -> Tuple[int, int]:
        return self.pos

    def get_dimensions(self) -> Tuple[int, int]:
        return self.duck_surface.get_size()

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.duck_surface, self.pos)

    def move(self, dx: float, dy: float) -> None:
        self.pos = (
            int(self.pos[0] + dx * self.speed),
            int(self.pos[1] + dy * self.speed)
        )

        screen_width, screen_height = pygame.display.get_surface().get_size()
        duck_width, duck_height = self.duck_surface.get_size()
        self.pos = (
            max(0, min(self.pos[0], screen_width - duck_width)),
            max(0, min(self.pos[1], screen_height - duck_height))
        )

    def clicked(self, click_pos: Tuple[int, int]) -> bool:
        selfx, selfy = self.pos
        clickx, clicky = click_pos

        duck_width, duck_height = self.duck_surface.get_size()

        if (selfx < clickx < selfx + duck_width
                and selfy < clicky < selfy + duck_height):
            return True
        return False

    def hide(self) -> None:
        self.duck_surface = None
        self.caught = True


class GoldenDuck(Duck):
    __dir = "Ducks/golden_duck.png"
    speed: float = 2

    def __init__(self, position: Tuple[int, int], scale: float = 0.4):
        super().__init__(position, scale)
        self.duck_surface = self._initialize()
        self.caught = False
        self.type = "golden"
