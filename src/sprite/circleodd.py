import constants
from .circlebase import CircleBase


class CircleOdd32(CircleBase):
    _COLLISION_RADIUS = 15.5
    _GETS_INPUT = True

    _COLOR = (155, 0, 0)

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

    def collide_CircleCollide(self, other):
        self._set_image((0, 155, 0))

    def update(self, dt, camera):
        self._set_image((155, 0, 0))
