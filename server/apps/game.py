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
    """A class used to represent a battleship gameboard
    
    Attributes:
        SIZE (int): board size constant
    """

    SIZE = 10

    def __init__(self):
        """Constructor method
        
        Initializes attributes to be constructed in other methods
        """
        self.board = self.create_board(Gameboard.SIZE) #: list of list representation of the gameboard
        self.fleet = Fleet() #: Fleet object representing this board's fleet

    def create_board(self, size):
        """Creates a list of list presentation of the gameboard
        
        Args:
            size (int): The size of the square board

        Returns:
            list of list: A representation of the gameboard
        """
        board = []
        for i in range(size):
            board.append([])
            for j in range(size):
                board[i].append("~")

        return board
    
    def get_board(self):
        """Gets the game's board list representation
        
        Returns:
            list of list: self.board
        """
        return self.board
    
    def get_secret_board(self):
        """Gets the game's board list representation without the ship's positions
        
        Returns:
            list of list: self.board without ship positions
        """
        secret_board = self.board.copy()
        for row in range(len(secret_board)):
            for column in range(len(secret_board)):
                if secret_board[row][column] == "S":
                    secret_board[row][column] = "~"

        return secret_board

    def place_fleet(self):
        """Positions the fleet on the board randomly

        Utilizes the nested functions is_placement_valid and find_ship_coordinates
        
        Args:
            fleet (Fleet): A player's fleet
            
        Returns:
            None
        """
        
        def is_placement_valid(coordinates):
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

        def find_ship_coordinates(ship):
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

                    if (is_placement_valid(coordinates)):
                        return coordinates

            elif direction == "vertical":
                while True:
                    # The initial square of the ship's coordinates
                    [row, column] = [randrange(0, 10 - offset), randrange(0, 10)]
                    # The full range of the ship's coordinates
                    coordinates = [[row + i, column] for i in range(offset)]

                    if (is_placement_valid(coordinates)):
                        return coordinates

        for ship in self.fleet.__dict__.values():
            coordinates = find_ship_coordinates(ship)
            ship.set_coordinates(coordinates)
            for coordinate in coordinates:
                self.board[coordinate[0]][coordinate[1]] = "S"

    def attack_coordinate(self, coordinate):
        """Attacks the specified coordinate
        
        Updates the board to represent the attacked coordinate and, if an attack hits a ship,
        calls the ship.hit() function 

        Args:
            coordinate (list): A [row, column] list representing a coordinate in the board

        Returns:
            bool: True if the coordinates for an attack are valid, False otherwise
        """

        def miss():
            """Represents a miss in the gameboard with an 'O'
            
            Returns:
                bool: True
            """
            self.board[coordinate[0]][coordinate[1]] = "O"
            return True
    
        def hit():
            """Represents a hit in the gameboard with an 'X' and calls the ship.hit() function
            
            Returns:
                bool: True
            """
            for ship in self.fleet.__dict__.values():
                if coordinate in ship.coordinates:
                    ship.hit()
            self.board[coordinate[0]][coordinate[1]] = "X"
            return True

        hit_square = self.board[coordinate[0]][coordinate[1]]

        if (hit_square == "O" or hit_square == "X"):
            return False
        
        if hit_square == "~":
            return miss()
        
        if hit_square == "S":
            return hit()
        
    def is_fleet_destroyed(self):
        """Checks if this board's fleet has been destroted

        Calls the is_destroyed method on the fleet to check
        
        Returns:
            bool: True if the whole fleet has been sunk, False otherwise
        """
        return self.fleet.is_destroyed()
    

class Game:
    """A class to represent a game"""

    def __init__(self):
        """Constructor method
        
        Creates both players' boards
        """
        player1_board = Gameboard()
        player2_board = Gameboard()
        turn = 1