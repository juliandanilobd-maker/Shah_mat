from app.domain.player.player import Player

class HumanPlayer(Player):

    def get_action(self):

        print(f"{self.name}, selecciona una acción")

        action_type = input('MOVE o ATTACK:')

        return {"type": action_type.upper}