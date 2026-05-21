from app.domain.player.human_player import HumanPlayer
from app.domain.player.ai_player import AIPlayer

class TurnManager:

    def __init__(self):
        self.players = []
        self.current_index = 0

    def setup_players(self, mode):

        if mode == 'PVP':

            self.players = [
                HumanPlayer("Jugador 1"),
                HumanPlayer("Jugador 2")
            ]

        elif mode == 'PLAYER VS CPU':

            self.players = [
                HumanPlayer("Jugador 1"),
                AIPlayer("CPU")
            ]
            
    def get_current_player(self):

        current_player = self.players[self.current_index]
        return current_player
    
    def next_turn(self):
        self.current_index = (self.current_index + 1) % len(self.players)