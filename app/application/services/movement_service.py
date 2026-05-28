from app.domain.board.move import Move
from app.domain.board.board import Board

# Esta clase no tiene estado, solo valida datos que le envian, por tanto no necesitamos
# argumentos de inicializacion


class MovementService:
    # Iniciamos creando una función que determina si el movimiento
    # seleccionado es valido
    def validate_move(self, board: Board, move: Move, player: str) -> bool:

        # Si no hay nada en la casilla de origen, no hay pieza que mover
        piece = board.get_piece(move.origin)

        if piece is None:
            return False

        # Se establece primero si es que el jugador que quiere hacer
        # el movimiento es el jugador actual
        if piece.owner != player:
            return False

        # Determinar la casilla destino está dentro de los límites del tablero
        if not board.is_within_bounds(move.destination):
            return False

        # Calculamos la distancia del movimiento con la formula Manhattan

        distance = move.distance()

        if distance > piece.movement_range:
            return False
        return True
