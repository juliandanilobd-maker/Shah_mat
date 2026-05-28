import pytest
from app.domain.board.move import Move
from app.domain.board.position import Position


class TestMove:

    # Comprobar si se reconocen movimientos a casillas no validas,
    # en este caso casilla 0
    def test_is_null_move(self):
        position = Position(2, 2)
        move = Move(position, position)
        assert move.is_null_move() is True

    # Comprobar si se reconocen casillas validas
    def test_no_is_null_move(self):
        move = Move(Position(0, 0), Position(1, 1))
        assert move.is_null_move() is False

    # Comprobar si la funcion distancia en Move llama correctamente a la funcion
    # manhattan_distance en Position
    def test_distance_move(self):
        move = Move(Position(0, 0), Position(3, 4))
        assert move.distance() == 7

    # Definir si los valores de movimiento permanece inmutables por el uso de
    # @dataclass(frozen=True)
    def test_move_inmutable(self):
        move = Move(Position(0, 0), Position(1, 1))
        with pytest.raises(Exception):
            move.origin = Position(5, 5)
