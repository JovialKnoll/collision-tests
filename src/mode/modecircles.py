import jovialengine
import pygame

import constants
from sprite import CircleCollide, Circle32Even, Circle32Odd, Circle31Even, Circle31Odd


class ModeCircles(jovialengine.ModeBase):
    def __init__(self):
        super().__init__()
        self._background.fill(constants.WHITE)
        circle = CircleCollide(topleft=(316, 182))
        circle.start(self)
        circle = Circle32Even(topleft=(332, 212))
        circle.start(self)
        circle = Circle31Even(topleft=(332, 152))
        circle.start(self)
        circle = Circle32Odd(topleft=(300, 212))
        circle.start(self)
        circle = Circle31Odd(topleft=(300, 152))
        circle.start(self)

    def _take_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            from .modecollisions import ModeCollisions
            self.next_mode = ModeCollisions()
