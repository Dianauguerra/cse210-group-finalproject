import arcade
import constants
from game.directing.game import Game

def main():

    # Creates the game and starts it going.
    window = Game( constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT )
    arcade.run()

if __name__ == "__main__":
    main()