import pygame


class Camera:

    def __init__(self, raiders_game) -> None:
        self.screen = raiders_game.screen
        self.screen_rect = raiders_game.screen.get_rect()

        self.settings = raiders_game.settings
    
        # TODO: Move image selection to settings.py ??
        self.image = pygame.image.load('images/shutterOpenedSmall.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False


    def update_position(self):
        if self.moving_right == True:
            self.x += self.settings.camera_speed
        if self.moving_left == True:
            self.x -= self.settings.camera_speed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    