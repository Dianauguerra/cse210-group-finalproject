import random
import constants
import arcade
from game.casting.actor import Actor

class Meteorite( Actor ):
    """A thing, moveable meteorite that participates in the game. 
    
    The responsibility of Meteorite is to draw itself, keep track of its position and velocity.

    Attributes:
        center._y( Point ): The random position for y.
        _velocity.dx( Point ): The random speed and direction for x.
        _velocity.dy( Point ): 0.
        _radius( int ): The radius of the target.
    """

    def __init__( self ):
        """Constructs a new Meteorite."""
        super().__init__()
        self.center._y = random.uniform( constants.SCREEN_HEIGHT / 4, constants.SCREEN_HEIGHT )
        self._velocity.dx = random.uniform( 1, 3 )
        self._velocity.dy = 0
        self._radius = constants.METEORIT_RADIUS

    def draw( self ):
        """Draw the object itself on screen."""

        # Load the image.
        image = arcade.load_texture( constants.METEORIT_IMAGE )

        # State the scale.
        scale = .05

        # Draw the object on screen.
        arcade.draw_texture_rectangle( self.center._x, self.center._y, scale * image.width, scale * image.height, image, self._angle )

    def advance( self, reverse = True ):
        """Moves the fly object to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            center._x( int ): The maximum x value.
            center._y( int ): The maximum y value.
        """
        # Move the flying object forward.
        if reverse:
            self.center._x += self._velocity.dx
            self.center._y += self._velocity.dy
        else:
            self.center._x -= self._velocity.dx
            self.center._y -= self._velocity.dy