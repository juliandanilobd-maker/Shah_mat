from app.domain.units.king import King


class VictoryService:

    # definimos una funcion que busque los reyes en el tablero y otorgue la victoria
    # si el rey enemigo esta derribado
    def check_victory(self, board) -> str | None:
        kings_alive = {}

        for _position, piece in board.get_all_pieces():
            if isinstance(piece, King) and piece.is_alive():
                kings_alive[piece.owner] = True

        if "Jugador 1" not in kings_alive:
            return "Jugador 2"

        if "Jugador 2" not in kings_alive:
            return "Jugador 1"

        return None

    # funcion que devuelve game over
    def is_game_over(self, board) -> bool:

        return self.check_victory(board) is not None
