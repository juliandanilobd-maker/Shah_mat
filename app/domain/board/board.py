from app.domain.board.position import Position


class Board:

    def __init__(self, size: int = 10):

        self.size = size
        self.grid = self.create_board()

    # Creamos la función que crea el tablero
    def create_board(self):
        return [[None for _ in range(self.size)] for _ in range(self.size)]

    # Colocar piezas iniciales
    def setup_initial_state(self):
        pass

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

    def render(self):
        print("\nTABLERO:")
        for row in self.grid:
            print(["." if cell is None else "P" for cell in row])
