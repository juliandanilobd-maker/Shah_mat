from app.domain.board.position import Position
from app.domain.units.lancer import Lancer
from app.domain.units.light_cavalry import LightCavalry
from app.domain.units.heavy_cavalry import HeavyCavalry
from app.domain.units.king import King


class Board:

    def __init__(self, size: int = 10):

        self.size = size
        self.grid = self.create_board()

    # Creamos la función que crea el tablero
    def create_board(self):
        return [[None for _ in range(self.size)] for _ in range(self.size)]

    # Colocar piezas iniciales
    def setup_initial_state(self):
        """
        Disposición inicial del tablero 10x10

        Jugador 1 (fila 0-1, parte superior):
            Fila 0: .Rey Centro, Caballeria pesada a los lados, Caballeria ligera en los
            extremos
            Fila 1: Lanceros en columnas pares como linea de frente

        Jugador 2 (fila 8-9, parte inferior, espejo):
            Fila 8: .Rey Centro, Caballeria pesada a los lados, Caballeria ligera en los
            extremos
            Fila 9: Lanceros en columnas pares como linea de frente

        Columnas: 0    2    4    6    8
        Fila 0:   CL   CP   REY  CP   CL
        Fila 1:   L    L    L    L    L
        ...
        Fila 8:   L    L    L    L    L
        Fila 9:   CL   CP   REY  CP   CL
        """

        self.place_piece(Position(0, 0), LightCavalry("Jugador 1"))
        self.place_piece(Position(0, 2), HeavyCavalry("Jugador 1"))
        self.place_piece(Position(0, 4), King("Jugador 1"))
        self.place_piece(Position(0, 6), HeavyCavalry("Jugador 1"))
        self.place_piece(Position(0, 8), LightCavalry("Jugador 1"))

        for col in range(0, 10, 2):
            self.place_piece(Position(1, col), Lancer("Jugador 1"))

        self.place_piece(Position(9, 0), LightCavalry("Jugador 2"))
        self.place_piece(Position(9, 2), HeavyCavalry("Jugador 2"))
        self.place_piece(Position(9, 4), King("Jugador 2"))
        self.place_piece(Position(9, 6), HeavyCavalry("Jugador 2"))
        self.place_piece(Position(9, 8), LightCavalry("Jugador 2"))

        for col in range(0, 10, 2):
            self.place_piece(Position(8, col), Lancer("Jugador 2"))

    # Creamos una función para ver su la posición está dentro de los límites del tablero
    def is_within_bounds(self, position) -> bool:

        return 0 <= position.row < self.size and 0 <= position.col < self.size

    # Determinar si una casilla está vacía
    def is_empty(self, position) -> bool:

        if not self.is_within_bounds(position):
            return False

        return self.grid[position.row][position.col] is None

    # Función para determinar si en cierta ubicacion, que pieza existe en esa
    def get_piece(self, position: Position):

        if not self.is_within_bounds(position):
            return None
        return self.grid[position.row][position.col]

    # Función para modificar el tablero y establecer que una pieza va a ocupar una
    # casilla
    def place_piece(self, position: Position, piece) -> bool:
        if not self.is_within_bounds(position):
            return False

        if not self.is_empty(position):
            return False

        self.grid[position.row][position.col] = piece
        return True

    # Función para mover la pieza
    def move_piece(self, origin: Position, destination: Position) -> bool:

        if not self.is_within_bounds(origin) or not self.is_within_bounds(destination):
            return False

        piece = self.get_piece(origin)
        if piece is None:
            return False

        if not self.is_empty(destination):
            return False
        self.grid[destination.row][destination.col] = piece
        self.grid[origin.row][origin.col] = None
        return True

    # Establecemos una funcion que muestra todas las piezas vivas en el tablero
    def get_all_pieces(self) -> list:

        pieces = []
        for row in range(self.size):
            for col in range(self.size):
                piece = self.grid[row][col]
                if piece is not None:
                    pieces.append((Position(row, col), piece))
        return pieces

    def render(self):
        print("\nTABLERO:")
        for row in self.grid:
            print(["." if cell is None else "P" for cell in row])
