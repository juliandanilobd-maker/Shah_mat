import pytest

from app.domain.match.match import Match


class FakePiece:
    def __init__(self, owner="jugador1", defense=2, attack_value=5):
        self.owner = owner
        self.defense = defense
        self.attack_value = attack_value

    def recieve_attack(self, attack: int) -> bool:
        return attack > self.defense


@pytest.fixture
def sample_match():
    match = Match(mode="PVP")
    match.initialize()
    return match


# Prueba para determinar si se inicializa la partida
def test_match_initialization(sample_match):

    assert sample_match.mode == "PVP"
    assert sample_match.finished is False


# Prueba para determinar si cuando se inicia se establece el tablero y los jugadores
def test_initialize_sets_board_and_players(sample_match):

    assert sample_match.board is not None
    assert len(sample_match.turn_manager.players) == 2


# Prueba para determinar si se procesa el movimiento de la pieza
def test_process_attack_action(sample_match):

    attacker = FakePiece(owner="jugador1", attack_value=5)
    defender = FakePiece(owner="jugador2", defense=2)

    action = {"type": "ATTACK", "attacker": attacker, "defender": defender}

    result = sample_match.process_action(action)

    assert result["type"] == "DAMAGE"


# Prueba para determinar que al iniciar una partida no se finaliza
def test_finished_returns_false_initially(sample_match):

    assert sample_match.is_finished() is False
