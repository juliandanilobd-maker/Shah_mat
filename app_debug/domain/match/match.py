from app.domain.board.board import Board
from app.domain.combat.combat_system import CombatSystem
from app.domain.turn.turn_manager import TurnManager


class Match:

    def __init__(self, mode):

        self.mode = mode
        self.board = Board()
        self.combat = CombatSystem()
        self.turn_manager = TurnManager()
        self.finished = False

    def initialize(self):
        self.board.setup_initial_state()
        self.turn_manager.setup_players(self.mode)

    def process_action(self, action):

        if action["type"] == "MOVE":
            return self.board.validate_move(action)

        if action["type"] == "ATTACK":
            return self.combat.prepare_attack(action)

    def apply_result(self, result):

        if result["type"] == "DAMAGE":
            self.board.apply_damage(result)

    def is_finished(self):
        return self.finished

    def finish(self):
        print("Guardando resultados...")
