class Velocity:
    """The velocity of something.

    The responsibility of Velocity is to hold and provide information about itself.

    Attributes:
        dx ( integer ): The horizontal velocity.
        dy ( integer ): The vertical velocity.
    """
    def __init__(self):
        """Constructs a new Velocity using the specified dx and yy values.
        
        Args:
            dx ( int ): The specified x value.
            dy ( int ): The specified y value.
        """
        self.dx = 0.0
        self.dy = 0.0