import constants
import arcade
from threading import Timer
from game.casting.actor import Actor

class Square_Timer( Actor ):
    """A rectangle, that represents a timer for the game. 
    
    The responsibility of Square_Timer is to draw itself, keep track of its position and move itself.

    Attributes:
        center._y( Point ): The random position for y.
        velocity.dx( Point ): The random speed and direction for x.
        velocity.dy( Point ): The random speed and direction for y.
        radius( int ): The radius of the target.
    """
    def __init__( self ):
        """Constructs a new Square_Timer."""
        super().__init__()
        self._time = constants.RACE_TIME
        self.center._x = constants. SCREEN_WIDTH / 2
        self.center._y = constants.SCREEN_HEIGHT / 2
        self.advance()

    def draw( self ):
        """Draw the object itself on screen."""
        # Draw the object on screen.
        arcade.draw_rectangle_filled( self.center._x, self.center._y, constants.TIMER_WIDTH, constants.TIMER_HEIGHT, constants.TIMER_COLOR )
    
    def advance( self ):
        """Moves the Square_Timer object to its next position according to the time."""
        # Calculate the speed from screen height pixels.
        speed = abs( constants.SCREEN_HEIGHT / self._time )
        
        # Move the timer per second.
        self.center._y -= speed
        t = Timer( 1, self.advance )
        t.daemon = True
        t.start()
        if self.center._y < -( constants.SCREEN_HEIGHT / 2 ):
            t.cancel()