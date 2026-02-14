import constants
from .circlebase import CircleMove


class CircleEven32(CircleMove):
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
