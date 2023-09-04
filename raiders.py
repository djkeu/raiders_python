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

    