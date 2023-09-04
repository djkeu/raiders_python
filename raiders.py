print("\n\tRaiders of the Lost Gloves\n")

import sys
import pygame

from settings import Settings


class Raiders:
    """Class to manage the game."""

    def __init__(self) -> None:
        """Initialize the game and resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raiders of the Lost Gloves")

    def run_game(self):
        """Main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)

            pygame.display.flip()


if __name__ == '__main__':
    raiders = Raiders()
    raiders.run_game()
