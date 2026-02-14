import jovialengine
import pygame

import constants
from sprite import CircleEven32
from sprite import CircleOdd32


class ModeCircles(jovialengine.ModeBase):
    def __init__(self):
        super().__init__()
        self._background.fill(constants.WHITE)
        circle_even = CircleEven32(topleft=(332, 212))
        circle_even.start(self)
        circle_odd = CircleOdd32(topleft=(300, 212))
        circle_odd.start(self)

    def _take_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            from .modecollisions import ModeCollisions
            self.next_mode = ModeCollisions()
