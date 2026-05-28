from app.domain.board.move import Move
from app.domain.units.piece import Piece

# Se inicializa la clase hija con sus propios atributos, y se establece
# movimiento valido dentro del rango de movimiento


class HeavyCavalry(Piece):

    def __init__(self, owner: str):
        super().__init__(
            owner=owner,
            movement_range=2,
            defense=2,
            attack_value=2,
        )

    def can_move(self, move: Move) -> bool:
        if move is None or move.is_null_move():
            return False
        return move.distance() <= self.movement_range
