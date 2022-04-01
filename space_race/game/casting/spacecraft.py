import arcade
import constants
from game.casting.actor import Actor

class Spacecraft( Actor ):
    """
    The Spacecraft is a rectangle that tracks some keyboard keys and move itself.

    Attributes:
        center( Point ): The center screen coordinates.
    """
    def __init__( self, position ):
        """Constructs a new Spacecraft."""
        super().__init__()
        self.center._x = position
        self.center._y = constants.START_POSITION

        # Track the current state of what key is pressed.
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = constants.PLAYERS_SPEED

    def draw( self ):
        """Draw the object itself on screen."""
        
        # Load the image.
        image = arcade.load_texture( constants.SPACECRAFT_IMAGE )

        # State the scale.
        scale = .08

        # Draw the object on screen.
        arcade.draw_texture_rectangle( self.center._x, self.center._y, scale * image.width, scale * image.height, image, self._angle + 45 )