import jovialengine

import constants


class CircleOdd32(jovialengine.GameSprite):
    # just using constants.SPRITE_PLAYER to start this as a 32x32 sprite
    _IMAGE_LOCATION = constants.SPRITE_PLAYER
    _ALPHA_OR_COLORKEY = False
    _COLLISION_RADIUS = 15.5
    _GETS_INPUT = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._set_image((155, 0, 0))

    def _set_image(self, color: tuple[int, int, int]):
        self.image = self.mask.to_surface(setcolor=color, unsetcolor=constants.COLORKEY)
        self.image.set_colorkey(constants.COLORKEY)

    def _take_state_change(self, state_change):
        # pixel-precise movement
        if state_change.new_value == 1:
            dx = 0
            dy = 0
            if state_change.event_type == constants.EVENT_LEFT_2:
                dx -= 1
            elif state_change.event_type == constants.EVENT_RIGHT_2:
                dx += 1
            elif state_change.event_type == constants.EVENT_UP_2:
                dy -= 1
            elif state_change.event_type == constants.EVENT_DOWN_2:
                dy += 1
            self.rect.move_ip(dx, dy)
