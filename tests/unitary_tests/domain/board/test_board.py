from app.domain.board.board import Board
from app.domain.board.position import Position


# Se crea una clase pieza falsa para testear las funciones del tablero
class FakePiece:

    def __init__(self, owner="player1"):
        self.owner = owner


class TestBoard:

    def setup_method(self):
        self.board = Board()
        self.piece = FakePiece()

    # Prueba para determinar si se crea el tablero con las medidas adecuadas
    def test_create_board_size(self):

        board = Board()

        assert len(board.grid) == 10
        assert len(board.grid[0]) == 10

    # Prueba para determinar si el tablero se crea sin valores en sus casillas
    def test_board_initial_values_none(self):

        board = Board()

        for row in board.grid:
            for cell in row:
                assert cell is None

    # Prueba para determinar si una casilla inicia vacia
    def test_initial_empty_grid(self):
        assert self.board.is_empty(Position(3, 3)) is True

    # Prueba para definir si una casilla esta ocupada
    def test_occupied_grid(self):
        position = Position(3, 3)
        self.board.place_piece(position, self.piece)
        assert self.board.is_empty(position) is False

    # Prueba para determinar si se reconocen las casillas dentro de los limites
    def test_is_within_bounds(self):
        assert self.board.is_within_bounds(Position(0, 0)) is True
        assert self.board.is_within_bounds(Position(9, 9)) is True
        assert self.board.is_within_bounds(Position(5, 5)) is True

    # Determinar si ser reconocen las casillas fuera de los limites
    def test_is_not_within_bounds(self):
        assert self.board.is_within_bounds(Position(-1, 0)) is False
        assert self.board.is_within_bounds(Position(0, -1)) is False

    def test_is_out_of_bound(self):
        assert self.board.is_within_bounds(Position(10, 0)) is False
        assert self.board.is_within_bounds(Position(0, 10)) is False

    # Prueba para determinar que una casilla fuera de limites no es vacia
    def test_out_of_bounds_grid_is_not_empty(self):
        position = Position(99, 99)
        assert self.board.is_empty(position) is False

    # No se puede colocar una pieza en una casilla ocupada
    def test_piece_in_occupied_grid(self):
        position = Position(1, 1)
        self.board.place_piece(position, self.piece)
        result = self.board.place_piece(position, FakePiece())
        assert result is False

    # Si se devuelve la posicion de una pieza
    def test_get_piece(self):
        position = Position(2, 2)
        self.board.place_piece(position, self.piece)
        assert self.board.get_piece(position) == self.piece

    # Comrpobar que no se puede obtener la posicion de una pieza de una casilla vacia
    def test_get_piece_empty_grid(self):
        assert self.board.get_piece(Position(5, 5)) is None

    # Comprobar que no se puede obtener una pieza fuera de limites
    def test_get_piece_out_of_bounds(self):
        assert self.board.get_piece(Position(99, 99)) is None

    # Comprobar si se mueve una pieza de forma correcta
    def test_move_piece(self):
        origin = Position(0, 0)
        destination = Position(0, 3)
        self.board.place_piece(origin, self.piece)
        result = self.board.move_piece(origin, destination)
        assert result is True
        assert self.board.get_piece(destination) == self.piece
        assert self.board.get_piece(origin) is None

    # Comprobar que no se mueve una pieza de una casilla de origen sin piezas
    def test_move_piece_empty_origin(self):
        result = self.board.move_piece(Position(0, 0), Position(1, 1))
        assert result is False

    # Comprobar que no se puede mover una pieza a una casilla ocupada
    def test_move_piece_occupied_grid(self):
        origin = Position(0, 0)
        destination = Position(0, 1)
        self.board.place_piece(origin, self.piece)
        self.board.place_piece(destination, FakePiece())
        result = self.board.move_piece(origin, destination)
        assert result is False

    # No se puede mover una pieza fuera de los limites del tablero
    def test_move_piece_out_of_bounds(self):
        origin = Position(0, 0)
        self.board.place_piece(origin, self.piece)
        result = self.board.move_piece(origin, Position(99, 99))
        assert result is False

    # Una vez se mueve una pieza a una casilla, se borra el resgistro de su origen
    # No pueden existir piezas duplicadas, registradas en su origen y en su destino
    def test_move_piece_no_duplicate(self):
        origin = Position(3, 3)
        destination = Position(7, 7)
        self.board.place_piece(origin, self.piece)
        self.board.move_piece(origin, destination)
        assert self.board.get_piece(origin) is None
        assert self.board.get_piece(destination) == self.piece
