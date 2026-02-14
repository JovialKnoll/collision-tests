import jovialengine

import constants


class CircleEven32(jovialengine.GameSprite):
    # just using constants.SPRITE_PLAYER to start this as a 32x32 sprite
    _IMAGE_LOCATION = constants.SPRITE_PLAYER
    _ALPHA_OR_COLORKEY = False
    _COLLISION_RADIUS = 16
    _GETS_INPUT = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._set_image((255, 0, 0))

    def _set_image(self, color: tuple[int, int, int]):
        self.image = self.mask.to_surface(setcolor=color, unsetcolor=constants.COLORKEY)
        self.image.set_colorkey(constants.COLORKEY)

    def _take_state_change(self, state_change):
        # pixel-precise movement
        if state_change.new_value == 1:
            dx = 0
            dy = 0
            if state_change.event_type == constants.EVENT_LEFT:
                dx -= 1
            elif state_change.event_type == constants.EVENT_RIGHT:
                dx += 1
            elif state_change.event_type == constants.EVENT_UP:
                dy -= 1
            elif state_change.event_type == constants.EVENT_DOWN:
                dy += 1
            self.rect.move_ip(dx, dy)

    def collide_CircleCollide(self, other):
        self._set_image((0, 255, 0))

    def update(self, dt, camera):
        self._set_image((255, 0, 0))
