import pygame

import constants
from .modebigger import ModeBigger
from sprite import Player


class ModeCollisions(ModeBigger):
    def __init__(self):
        super().__init__()
        self._background.fill(constants.WHITE)
        player = Player(center=(64, 64))
        player.start(self)

    def _take_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            from .modecircles import ModeCircles
            self.next_mode = ModeCircles()
