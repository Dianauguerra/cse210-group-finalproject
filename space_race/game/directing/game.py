import arcade
import random
import constants
from game.casting.spacecraft import Spacecraft
from game.casting.meteorite import Meteorite
from game.casting.score import Score
from game.casting.square_timer import Square_Timer

class Game( arcade.Window ):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Spacecraft
        Meteorite
        Point
        Velocity
        Score
        Square_Timer

    This class will then call the appropriate functions of
    each of the above classes.
    """

    def __init__( self, width, height ):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        :param title: Screen title
        """
        super().__init__( width, height, title = constants.GAME_NAME )

        self.game_over = False
        self.player1 = Spacecraft( constants.PLAYER_ONE_POSITION )
        self.player2 = Spacecraft( constants.PLAYER_TWO_POSITION )
        self.timer = Square_Timer()
        self.score1 = Score()
        self.score2 = Score()

        # Meteorites.
        self.left_targets = []
        self.right_targets = []

        arcade.set_background_color( constants.BACKGROUND_COLOR )

    def on_draw( self ):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """
        # Clear the screen to begin drawing.
        arcade.start_render()

        # draw each object
        self.player1.draw()
        self.player2.draw()

        # Draw all the meteorites.
        for target in self.left_targets:
            target.draw()
        for target in self.right_targets:
            target.draw()

        # Draw the scores.
        self.score1.draw( 10, constants.SCORE_POSITION, "Player One" )
        self.score2.draw( 700, constants.SCORE_POSITION, "Player Two" )

        self.timer.draw()

        if self.game_over:
            self.draw_game_over()

    def update( self, delta_time ):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_collisions()
        self.check_off_screen()

        # Decide if we should start a meteorite.
        if random.randint( 1, 15 ) == 1:
            self.create_target()

        # Move all the meteorites.
        for target in self.right_targets:
            target.advance()

        for target in self.left_targets:
            target.advance( False )
        
        # Rules for the move of the players.
        for player in [ self.player1, self.player2 ]:
            if player.up_pressed:
                player.center._y += player.speed * delta_time
            elif player.down_pressed:
                player.center._y -= player.speed * delta_time

    def create_target( self ):
        """
        Creates a new meteorite of a random type and adds it to the list.
        :return:
        """
        # Decide the type of meteorite to append.
        if random.randint( 1, 2 ) == 1:
            target = Meteorite()
            self.right_targets.append( target )
        elif random.randint( 1, 2 ) == 2:
            target = Meteorite()
            target.center._x = constants.SCREEN_WIDTH
            self.left_targets.append( target )

    def check_collisions(self):
        """
        Checks to see if players have hit meteorites.
        Removes dead items.
        :return:
        """
        for gamer in [ self.player1, self.player2 ]:
            for target in self.left_targets:

                    # Make sure they are both alive before checking for a collision
                    too_close = gamer._radius + target._radius

                    if ( abs( gamer.center._x - target.center._x ) < too_close and
                                abs( gamer.center._y - target.center._y ) < too_close ):

                        # Collision!
                        gamer.center._y = constants.START_POSITION
            
            for target in self.right_targets:

                    # Make sure they are both alive before checking for a collision
                    too_close = gamer._radius + target._radius

                    if ( abs( gamer.center._x - target.center._x ) < too_close and
                                abs( gamer.center._y - target.center._y ) < too_close ):
                        
                        #Collision!
                        gamer.center._y = constants.START_POSITION

    def check_off_screen( self ):
        """
        Checks to see if players or meteorites have left the screen
        and if so, removes them from their lists. If a player reach the top screen, add points to the score.
        :return:
        """
        for target in self.right_targets:
            if target.is_off_screen( constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT ):
                self.right_targets.remove( target )
        
        for target in self.left_targets:
            if target.is_off_screen( 0, constants.SCREEN_HEIGHT, True ):
                self.left_targets.remove( target )
        
        for player in [ self.player1, self.player2 ]:
            if player.is_off_screen( constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT ):

                # Return the player to start position.
                player.center._y = constants.START_POSITION

                if player == self.player1:
                    score = self.score1
                elif player == self.player2:
                    score = self.score2
                
                # Add points.
                if not self.game_over:
                    score._score += 1

        # Set game_over flag to True if the time ends.
        if not self.timer.is_off_screen( constants.SCREEN_WIDTH, -( constants.SCREEN_HEIGHT / 2 ) ):
            self.game_over = True
        
    def on_key_press( self, key, modifiers ):
        """Called whenever a key is pressed. """
        # If the player presses a key, update the speed.
        if key == arcade.key.W:
            self.player1.up_pressed = True
        elif key == arcade.key.S:
            self.player1.down_pressed = True
        elif key == arcade.key.I:
            self.player2.up_pressed = True
        elif key == arcade.key.K:
            self.player2.down_pressed = True

    def on_key_release( self, key, modifiers ):
        """Called when the user releases a key. """
        # If the player releases a key, update the speed.
        if key == arcade.key.W:
            self.player1.up_pressed = False
        elif key == arcade.key.S:
            self.player1.down_pressed = False
        elif key == arcade.key.I:
            self.player2.up_pressed = False
        elif key == arcade.key.K:
            self.player2.down_pressed = False

    def draw_game_over( self ):
        """Print the message "GAME OVER!" if the time ends."""
        gameover = constants.GAME_OVER_TEXT
        self.game_over = True
        start_x = 150
        start_y = constants.SCREEN_HEIGHT / 2
        arcade.draw_text( gameover, start_x, start_y, arcade.color.WHITE, constants.GAME_OVER_FONT_SIZE )