import constants
from game.shared.point import Point
from game.shared.velocity import Velocity

class Actor:
    """A visible, moveable thing that participates in the game. 
    
    The responsibility of Actor is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        center( Point ): The center screen coordinates.
        _velocity ( Point ): The speed and direction.
        _angle( int ): The angle at which the rifle should be aimed.
        _alive( bool ): If the object is alive or not.
        _radius( int ): The radius of the object.
    """
    def __init__( self ):
        """Constructs a new Actor."""
        self.center = Point( 0, 0 )
        self._velocity = Velocity()
        self._angle = constants.DEFAULT_ANGLE
        self._radius = constants.DEFAULT_RADIUS

    def draw( self ):
        """Draw the object itself on screen."""
        pass

    def advance( self ):
        """Moves the object to its next position."""
        pass
    
    def is_off_screen( self, screen_width, screen_height, reverse = False ):
        """Check if the object is still present on the screen.

        Args:
            screen_width( int ): The screen width.
            screen_height( int ): The screen height.
        """
        # Select the correc condition.
        if reverse:
            condition = self.center._x < screen_width
        else:
            condition = self.center._x > screen_width

        # Check whether the flying object is on screen or not.
        if ( condition or self.center._y > screen_height ):
            return True
        else:
            return False