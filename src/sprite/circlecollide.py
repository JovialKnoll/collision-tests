import jovialengine

import constants


class CircleCollide(jovialengine.GameSprite):
    # just using constants.SPRITE_PLAYER to start this as a 32x32 sprite
    _IMAGE_LOCATION = constants.SPRITE_PLAYER
    _ALPHA_OR_COLORKEY = False
    _COLLISION_RADIUS = 16

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._set_image((0, 0, 0))

    def _set_image(self, color: tuple[int, int, int]):
        self.image = self.mask.to_surface(setcolor=color, unsetcolor=constants.COLORKEY)
        self.image.set_colorkey(constants.COLORKEY)
