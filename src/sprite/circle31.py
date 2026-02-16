import pygame

from .circle32 import Circle32Even, Circle32Odd


class Circle31Even(Circle32Even):
    _COLLISION_RADIUS = 15
    _COLOR = (255, 0, 0)
    _COLOR_COLLIDE = (0, 255, 0)

    def draw_dynamic(self, screen, offset):
        center_point = round(pygame.Vector2(self.rect.topleft)) + (15, 15) + offset
        screen.set_at(center_point, (0, 0, 0))


class Circle31Odd(Circle32Odd):
    _COLLISION_RADIUS = 14.5
    _COLOR = (155, 0, 0)
    _COLOR_COLLIDE = (0, 155, 0)

    def draw_dynamic(self, screen, offset):
        center_point = round(pygame.Vector2(self.rect.topleft)) + (15, 15) + offset
        screen.set_at(center_point, (0, 0, 0))
