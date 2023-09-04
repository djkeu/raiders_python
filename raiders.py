# Try it yourself 12.1 Blue sky, p.238
print("\n\tRaiders of the Lost Gloves\n")

import sys
import pygame

class Raiders:
    """Class to manage the game."""

    def __init__(self) -> None:
        """Initialize the game and resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((960, 640))
        pygame.display.set_caption("Raiders of the Lost Gloves")

        self.bg_color = (230, 230, 130)

    def run_game(self):
        """Main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit()

            self.screen.fill(self.bg_color)

            pygame.display.flip()

if __name__ == '__main__':
    raiders = Raiders()
    raiders.run_game()
