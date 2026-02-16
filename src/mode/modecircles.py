import jovialengine
import pygame

import constants
from sprite import CircleCollide, Circle32Even, Circle32Odd


class ModeCircles(jovialengine.ModeBase):
    def __init__(self):
        super().__init__()
        self._background.fill(constants.WHITE)
        circle_collide = CircleCollide(topleft=(316, 182))
        circle_collide.start(self)
        circle_even = Circle32Even(topleft=(332, 212))
        circle_even.start(self)
        circle_odd = Circle32Odd(topleft=(300, 212))
        circle_odd.start(self)

    def _take_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            from .modecollisions import ModeCollisions
            self.next_mode = ModeCollisions()
