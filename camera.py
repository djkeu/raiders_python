import pygame


class Camera:
    """Class to manage the camera."""

    def __init__(self, raiders_game) -> None:
        """Initialize the camera and its starting position."""
        self.screen = raiders_game.screen
        self.screen_rect = raiders_game.screen.get_rect()
    
        self.image = pygame.image.load('images/shutterOpenedSmall.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """Draw the camera at its current position."""
        self.screen.blit(self.image, self.rect)
    