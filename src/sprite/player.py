import jovialengine

import constants


class Player(jovialengine.GameSprite):
    _IMAGE_LOCATION = ''
    _ALPHA_OR_COLORKEY = constants.COLORKEY
    _COLLISION_MASK_LOCATION = ''
    _COLLISION_MASK_ALPHA_OR_COLORKEY = constants.COLORKEY
    _GETS_INPUT = True

    def update(self, dt: int):
        dx = 0
        dy = 0
        if self._input_frame.get_input_state(0, constants.EVENT_LEFT) == 1:
            dx -= 32 * 0.001 * dt
        if self._input_frame.get_input_state(0, constants.EVENT_RIGHT) == 1:
            dx += 32 * 0.001 * dt
        if self._input_frame.get_input_state(0, constants.EVENT_UP) == 1:
            dy -= 32 * 0.001 * dt
        if self._input_frame.get_input_state(0, constants.EVENT_DOWN) == 1:
            dy += 32 * 0.001 * dt
        self.pos_x += dx
        self.pos_y += dy
