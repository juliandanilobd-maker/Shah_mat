from app.application.services.combat_service import CombatService
from app.application.services.movement_service import MovementService
from app.domain.turn.turn_manager import TurnManager
from app.domain.board.board import Board


class Match:

    def __init__(self, mode):

        self.mode = mode
        self.combat_service = CombatService()
        self.movement_service = MovementService()
        self.turn_manager = TurnManager()
        self.board = Board()
        self.finished = False

    def initialize(self):
        self.board.setup_initial_state()
        self.turn_manager.setup_players(self.mode)

    def process_action(self, action):

        player = self.turn_manager.get_current_player()

        if action["type"] == "DAMAGE":
            return self.movement_service.validate_move(
                self.board, action["damage"], player.name
            )

        if action["type"] == "ATTACK":
            return self.combat_service.attack(action["attacker"], action["defender"])

    def is_finished(self):
        return self.finished

    def finish(self):
        print("Guardando resultados...")
