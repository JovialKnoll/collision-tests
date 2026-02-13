import jovialengine
import pygame

import constants
from sprite import CircleEven


class ModeCircles(jovialengine.ModeBase):
    def __init__(self):
        super().__init__()
        self._background.fill(constants.WHITE)
        circle_even = CircleEven(center=(480, 270))
        circle_even.start(self)

    def _take_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            from .modecollisions import ModeCollisions
            self.next_mode = ModeCollisions()
