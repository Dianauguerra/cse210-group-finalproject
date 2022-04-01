import constants
import arcade
from game.casting.actor import Actor
from game.shared.point import Point

class Score( Actor ):
    """
    A record of points made for a player. 
    
    The responsibility of Score is to keep track of the points the player has earned by moving.
    It contains methods for drawing itself.

    Attributes:
        _score ( int ): The points earned in the game.
        _position( Point ): The position screen coordinates.
    """
    def __init__( self ):
        super().__init__()
        self._score = 0
        self._position = Point( 0, 0 )

    def draw( self, x, y, player ):
        """Puts the current score on the screen."""
        score_text = f"{player}: {self._score}"
        start_y = constants.SCREEN_HEIGHT - y

        # Change score color.
        arcade.draw_text( score_text, x, start_y, constants.SCORE_COLOR, constants.SCORE_FONT_SIZE )