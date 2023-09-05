print("\n\tRaiders of the Lost Gloves\n")

import sys
import pygame

from settings import Settings
from camera import Camera


class Raiders:
    """Class to manage Raiders of the Lost Gloves."""

    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raiders of the Lost Gloves")

        self.camera = Camera(self)

    def run_game(self):
        game_running = True

        while game_running:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
                # Quit game
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit()
                
                # TODO: Make movement continuous
                # Move the camera to the right
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.camera.rect.x += 5
                
                # Move the camera to the left
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.camera.rect.x -= 5

    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.camera.blitme()

            pygame.display.flip()
        

if __name__ == '__main__':
    rlg = Raiders()  # Raiders of the Lost Gloves
    rlg.run_game()
