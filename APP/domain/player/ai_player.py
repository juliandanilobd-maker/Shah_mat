from app.domain.player.player import Player

class AIPlayer(Player):

    def get_action(self):

        print(f"{self.name} está pensando...")

        return {"type": "MOVE"}