import pytest
from app.domain.board.position import Position


class TestPosition:

    # Función para determinar funcionamiento general de la formula manhattan
    def test_manhattan_distance_same_point(self):

        position = Position(3, 3)
        assert position.manhattan_distance(position) == 0

    # Comprueba un valor correcto del calculo de movimiento en fila
    def test_manhattan_distance_horizontal(self):
        a = Position(0, 0)
        b = Position(0, 4)
        assert a.manhattan_distance(b) == 4

    # Comprueba un valor correcto del calculo de movimiento en columna
    def test_manhattan_distance_y(self):
        a = Position(0, 0)
        b = Position(5, 0)

        assert a.manhattan_distance(b) == 5

    # Comprueba un calculo correcto de diagonales
    def test_manhattan_distance_diagonal(self):
        a = Position(0, 0)
        b = Position(3, 4)

        assert a.manhattan_distance(b) == 7

    # En la clase Position usamos @dataclass(frozen=True),
    # para que los datos sean inmutables,
    # eso se comprueba en lo siguiente
    def test_position_inmutable(self):
        position = Position(1, 1)
        with pytest.raises(Exception):
            position.row = 99

    # Definir si se aplican la funcion de @dataclass correctamente:
    # generacion automatica de __eq__
    # Si se reconocen posiciones iguales
    def test_equal_positions(self):
        assert Position(2, 3) == Position(2, 3)

    # Definir si se reconocen posiciones diferentes
    def test_different_positions(self):
        assert Position(2, 3) != Position(3, 2)
