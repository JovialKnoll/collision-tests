import jovialengine

import constants


class ModeCircles(jovialengine.ModeBase):
    def __init__(self):
        super().__init__()
        self._background.fill(constants.WHITE)
