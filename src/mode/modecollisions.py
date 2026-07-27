import jovialengine
import pygame

import constants
from .modebigger import ModeBigger
from sprite import Player


class ModeCollisions(ModeBigger):
    _STATIC_COLLISION_MASK_INFOS = (
        ("test", constants.BACKGROUND_COLLISIONS, constants.COLORKEY),
    )

    def __init__(self):
        super().__init__()
        self._background.fill(constants.WHITE)
        for info in self._STATIC_COLLISION_MASK_INFOS:
            image = jovialengine.load.image(info[1], info[2])
            self._background.blit(image)
        player = Player(center=(64, 64))
        player.start(self)

    def _take_event(self, event):
        super()._take_event(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            from .modecircles import ModeCircles
            self.next_mode = ModeCircles()
