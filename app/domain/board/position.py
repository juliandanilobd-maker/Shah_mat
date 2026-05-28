from dataclasses import dataclass


# Iniciamos volviendolo inmutable
@dataclass(frozen=True)
class Position:

    row: int
    col: int

    # Determina la distancia del movimiento con la formula Manhattan
    def manhattan_distance(self, other: "Position") -> int:
        return abs(self.row - other.row) + abs(self.col - other.col)
