import jovialengine
import pygame

import constants
from sprite import CircleCollide, CircleEven32, CircleOdd32


class ModeCircles(jovialengine.ModeBase):
    __slots__ = (
        '_circle_even',
        '_circle_odd',
    )

    def __init__(self):
        super().__init__()
        self._background.fill(constants.WHITE)
        circle_collide = CircleCollide(topleft=(316, 182))
        circle_collide.start(self)
        self._circle_even = CircleEven32(topleft=(332, 212))
        self._circle_even.start(self)
        self._circle_odd = CircleOdd32(topleft=(300, 212))
        self._circle_odd.start(self)

    def _take_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            from .modecollisions import ModeCollisions
            self.next_mode = ModeCollisions()

    def _update_pre_draw(self):
        self._circle_even.set_image((255, 0, 0))
        self._circle_odd.set_image((155, 0, 0))
