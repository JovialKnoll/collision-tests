import jovialengine
import pygame

import constants


class ModeBigger(jovialengine.ModeBase):
    _SPACE_SIZE = (constants.SCREEN_SIZE[0] * 2, constants.SCREEN_SIZE[1] * 2)

    def _take_event(self, event):
        if event.type == pygame.KEYDOWN:
            match event.key:
                # number keys switch the camera to different quadrants of the space for testing purposes
                case pygame.K_1:
                    self._camera.topleft = (0, 0)
                case pygame.K_2:
                    self._camera.topleft = (constants.SCREEN_SIZE[0], 0)
                case pygame.K_3:
                    self._camera.topleft = (0, constants.SCREEN_SIZE[1])
                case pygame.K_4:
                    self._camera.topleft = (constants.SCREEN_SIZE[0], constants.SCREEN_SIZE[1])
