from app.domain.match.match import Match


class MatchController:

    def __init__(self, mode):
        self.match = Match(mode)

    def start(self):
        print("Iniciando partida...")

        self.match.initialize()

        self.game_loop()

    def game_loop(self):

        while not self.match.is_finished():

            player = self.match.turn_manager.get_current_player()

            print(f"\nTurno de: {player.name}")

            self.match.board.render()

            action = player.get_action()

            result = self.match.process_action(action)

            self.match.turn_manager.next_turn()

            return result

        print("FIN DE LA PARTIDA")
        self.match.finish()
