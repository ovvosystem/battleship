class Ship:
    """A class used to represent a ship"""

    def __init__(self, size):
        """Constructor method

        Args:
            size (int): The size of the ship
        """
        self.size = size
        self.times_hit = 0 #: Number of times ship has been hit