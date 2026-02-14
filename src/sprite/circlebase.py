import pygame
import jovialengine

import constants


class CircleBase(jovialengine.GameSprite):
    # just using constants.SPRITE_PLAYER to start this as a 32x32 sprite
    _IMAGE_LOCATION = constants.SPRITE_PLAYER
    _ALPHA_OR_COLORKEY = False
    _COLLISION_RADIUS = 16

    _COLOR = (48, 48, 48)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._set_image(self._COLOR)

    def _set_image(self, color: tuple[int, int, int]):
        self.image = self.mask.to_surface(setcolor=color, unsetcolor=constants.COLORKEY)
        self.image.set_colorkey(constants.COLORKEY)

    def draw_dynamic(self, screen, offset):
        first_center_point = round(pygame.Vector2(self.rect.topleft)) + (15, 15) + offset
        screen.set_at(first_center_point, (0, 0, 0))
        screen.set_at(first_center_point + (0, 1), (0, 0, 0))
        screen.set_at(first_center_point + (1, 0), (0, 0, 0))
        screen.set_at(first_center_point + (1, 1), (0, 0, 0))


class CircleMove(CircleBase):
    _GETS_INPUT = True
    _COLOR = (255, 0, 0)
    _COLOR_COLLIDE = (0, 255, 0)

    def collide_CircleCollide(self, other):
        self._set_image(self._COLOR_COLLIDE)

    def update(self, dt, camera):
        self._set_image(self._COLOR)
