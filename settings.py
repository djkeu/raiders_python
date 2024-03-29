class Settings:
    """Settings for Raiders of the Lost Gloves."""

    def __init__(self) -> None:
        """Initialize game settings."""
        # Screen settings
        self.bg_color = (230, 230, 130)
        self.screen_width = 960
        self.screen_height = 640
        self.caption = "Raiders of the Lost Gloves"

        # Camera settings
        self.camera_speed = 0.5
        self.camera_closed = 'images/shutterClosedSmall.png'
        self.camera_opened = 'images/shutterOpenedSmall.png'
