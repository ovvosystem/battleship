class Ship:
    """A class used to represent a ship"""

    def __init__(self, size):
        """Constructor method

        Args:
            size (int): The size of the ship
        """
        self.size = size
        self.times_hit = 0 #: Number of times ship has been hit
    
    def hit(self):
        """Increments the times_hit instance attribute

        Returns:
            None
        """
        self.times_hit += 1

    def is_sunk(self):
        """Checks if the ship has been sunk
        
        Returns:
            bool: True if it has been sunk, False otherwise
        """
        return self.times_hit == self.size