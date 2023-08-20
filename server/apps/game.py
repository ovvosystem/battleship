from random import choice, randrange

class Ship:
    """A class used to represent a ship"""

    def __init__(self, size):
        """Constructor method

        Args:
            size (int): The size of the ship
        """
        self.size = size
        self.times_hit = 0 #: Number of times ship has been hit
        self.coordinates = [] #: A list of the ship's coordinates, initially empty
    
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
    
    def set_coordinates(self, coordinates):
        """Sets the ship's coordinates
        
        Returns:
            None
        """
        self.coordinates = coordinates

    def get_coordinates(self):
        """Gets the ship's coordinates
        
        Returns:
            list: self.coordinates
        """
        return self.coordinates
    

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
        self.fleet = Fleet() #: Fleet object representing this board's fleet

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
    
    def is_placement_valid(self, coordinates):
        """Checks if a list of coordinates for a ship's placement are free

        Args:
            coordinates (list of list): A list containing different coordinates represented 
                                        as [row, column]

        Returns:
            bool: True if all the coordinates are free, False otherwise
        """
        for coordinate in coordinates:
            if self.board[coordinate[0]][coordinate[1]] != "~":
                return False
        
        return True

    def find_ship_coordinates(self, ship):
        """Finds valid coordinates for the ship's placement

        Args:
            ship (Ship): A ship of a player's fleet

        Returns:
            list: list of coordinates valid for the ship's placement
        """
        direction = choice(["horizontal", "vertical"])
        offset = ship.size

        if direction == "horizontal":
            while True:
                # The initial square of the ship's coordinates
                [row, column] = [randrange(0, 10), randrange(0, 10 - offset)]
                # The full range of the ship's coordinates
                coordinates = [[row, column + i] for i in range(offset)]

                if (self.is_placement_valid(coordinates)):
                    return coordinates

        elif direction == "vertical":
            while True:
                # The initial square of the ship's coordinates
                [row, column] = [randrange(0, 10 - offset), randrange(0, 10)]
                # The full range of the ship's coordinates
                coordinates = [[row + i, column] for i in range(offset)]

                if (self.is_placement_valid(coordinates)):
                    return coordinates