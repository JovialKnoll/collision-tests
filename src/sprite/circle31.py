import pygame

import constants
from .circle32 import Circle32Even, Circle32Odd


class Circle31Even(Circle32Even):
    _IMAGE_LOCATION = constants.SPRITE_31
    _COLLISION_RADIUS = 15
    _COLOR = (255, 0, 0)
    _COLOR_COLLIDE = (0, 255, 0)

    def draw_dynamic(self, screen, offset):
        basis = round(pygame.Vector2(self.rect.topleft)) + offset
        for x in (0, 15, 30):
            for y in (0, 15, 30):
                screen.set_at(basis + (x, y), constants.BLACK)


class Circle31Odd(Circle32Odd):
    _IMAGE_LOCATION = constants.SPRITE_31
    _COLLISION_RADIUS = 15.5
    _COLOR = (155, 0, 0)
    _COLOR_COLLIDE = (0, 155, 0)

    def draw_dynamic(self, screen, offset):
        basis = round(pygame.Vector2(self.rect.topleft)) + offset
        for x in (0, 15, 30):
            for y in (0, 15, 30):
                screen.set_at(basis + (x, y), constants.BLACK)
