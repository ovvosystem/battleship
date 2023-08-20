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
    

class Fleet:
    """A class to represent a player's full fleet
    
    fleets consist of a carrier (size 5), a battleship (size 4), a submarine (size 3),
    a cruiser (size 3), and a destroyer (size 2)
    """

    def __init__(self):
        """Constructor method"""
        self.carrier = Ship(5) #: Ship of size 5
        self.battleship = Ship(4) #: Ship of size 4
        self.submarine = Ship(3) #: Ship of size 3
        self.cruiser = Ship(3) #: Ship of size 3
        self.destroyer = Ship(2) #: Ship of size 2

    def is_destroyed(self):
        """Checks if all the fleet's ships have been sunk
        
        Returns:
            bool: True if the whole fleet has been sunk, False otherwise
        """
        return (self.carrier.is_sunk() and 
            self.battleship.is_sunk() and
            self.submarine.is_sunk() and
            self.cruiser.is_sunk() and
            self.destroyer.is_sunk())


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