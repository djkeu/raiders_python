print("\n\tRaiders of the Lost Gloves\n")

import sys
import pygame

from settings import Settings
from camera import Camera


class Raiders:
    """Class to manage the game."""

    def __init__(self) -> None:
        """Initialize the game and resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raiders of the Lost Gloves")

        self.camera = Camera(self)

    def run_game(self):
        """Main loop for the game."""

        while True:

            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Check for mouse and keyboard input."""
        for event in pygame.event.get():
                # Quit game
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit()
                
                # Move the camera to the right
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.camera.rect.x += 5
                
                # Move the camera to the left
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.camera.rect.x -= 5

    def _update_screen(self):
            """Update screen, flip to new screen."""
            self.screen.fill(self.settings.bg_color)
            self.camera.blitme()

            pygame.display.flip()
        

if __name__ == '__main__':
    raiders = Raiders()
    raiders.run_game()
