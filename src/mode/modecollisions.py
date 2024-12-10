import constants
from .modebigger import ModeBigger
from sprite import Player


class ModeCollisions(ModeBigger):
    def __init__(self):
        super().__init__()
        self._background.fill(constants.WHITE)
        player = Player((64, 64))
        player.start(self)
