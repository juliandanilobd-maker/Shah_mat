from app.domain.player.human_player import HumanPlayer


class TurnManager:

    def __init__(self):
        self.players = []
        self.current_index = 0

    def setup_players(self, mode: str):
        if mode == "PVP":
            self.players = [
                HumanPlayer("Jugador 1"),
                HumanPlayer("Jugador 2"),
            ]

    # Funcion para obtener el jugador actual
    def get_current_player(self):
        return self.players[self.current_index]

    # Calcular el siguiente turno
    def next_turn(self):
        self.current_index = (self.current_index + 1) % len(self.players)

    # Funcion que obtiene el numero de turno que se esta jugando
    def get_turn_number(self):
        return self.current_index + 1
