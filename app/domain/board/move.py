from dataclasses import dataclass
from app.domain.board.position import Position


@dataclass(frozen=True)
class Move:

    origin: Position
    destination: Position

    # Verifica si el movimiento deseado cambia la posicion de la pieza,
    # compara la posicion desde la que se parte y a la que se quiere llegar
    def is_null_move(self) -> bool:
        return self.origin == self.destination

    def distance(self) -> int:
        return self.origin.manhattan_distance(self.destination)
