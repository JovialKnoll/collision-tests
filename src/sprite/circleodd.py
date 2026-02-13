import jovialengine
from jovialengine.inputframe import StateChange

import constants


class CircleOdd(jovialengine.GameSprite):
    _GETS_INPUT = True

    def _take_state_change(self, state_change: StateChange):
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
                dx += 1
            self.rect.move_ip(dx, dy)
