from app.domain.board.move import Move
from app.domain.units.piece import Piece

# Se crea una clase hija de Piece,
# con sus propios valores de los atributos de defensa, ataque y rango de movimiento


class Lancer(Piece):

    def __init__(self, owner: str):
        super().__init__(
            owner=owner,
            movement_range=1,
            defense=1,
            attack_value=1,
        )

    # Se establece el rango de movimiento del lancero, solo en sentido horizontal
    # o vertical

    def can_move(self, move: Move) -> bool:
        if move is None or move.is_null_move():
            return False

        row_diff = move.destination.row - move.origin.row
        col_diff = move.destination.col - move.origin.col

        is_cardinal = (row_diff == 0) != (col_diff == 0)
        return is_cardinal and move.distance() <= self.movement_range
