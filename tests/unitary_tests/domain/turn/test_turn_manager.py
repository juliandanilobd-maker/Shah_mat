from app.domain.turn.turn_manager import TurnManager
from app.domain.player.human_player import HumanPlayer
from app.domain.player.ai_player import AIPlayer


# Prueba para definir que la clase HumanPlayer crea 2 jugadores
def test_pvp_creates_two_players():

    manager = TurnManager()

    manager.setup_players("PVP")

    assert isinstance(manager.players[0], HumanPlayer)
    assert isinstance(manager.players[1], HumanPlayer)


# Prueba para definir que la clase AIPlayer crea un player humano vs CPU
def test_pvp_creates_human_ai():

    manager = TurnManager()

    manager.setup_players("PLAYER VS CPU")

    assert isinstance(manager.players[0], HumanPlayer)
    assert isinstance(manager.players[1], AIPlayer)


# Prueba para definir si se asigna el turno correctamente
def test_get_current_player():

    manager = TurnManager()

    manager.setup_players("PVP")

    player = manager.get_current_player()

    assert player.name == "Jugador 1"
