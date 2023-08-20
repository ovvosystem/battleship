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
    

class Gameboard:
    """A class used to represent a battleship gameboard"""

    def __init__(self):
        """Constructor method
        
        Initializes attributes to be constructed in other methods
        """
        #: board (list of list): An empty list, to be constructed into a full gameboard
        #: in create_board method
        self.board = []

        #: ships (dict of Ship: list): An empty dict, to be expanded by the create_ship method
        self.ships = {}

    def create_board(self, size):
        """Creates a list of list presentation of the gameboard
        
        Args:
            size (int): The size of the square board

        Returns:
            None
        """
        for i in range(size):
            self.board.append([])
            for j in range(size):
                self.board[i].append("~")