from app.domain.match.match import Match
from tests.conftest import sample_match


# Prueba para determinar si se inicializa la partida
def test_match_initialization(sample_match):

    assert sample_match.mode == "PVP"
    assert sample_match.finished is False


# Prueba para determinar si cuando se inicia se establece el tablero y los jugadores
def test_initialize_sets_board_and_players(sample_match):

    assert sample_match.board is not None
    assert len(sample_match.turn_manager.players) == 2


# Prueba para determinar si se procesa el movimiento de la pieza
def test_process_move_action(sample_match):

    action = {"type": "MOVE"}

    result = sample_match.process_action(action)

    assert result["type"] == "MOVE_OK"


# Prueba para determinar que al iniciar una partida no se finaliza
def test_finished_returns_false_initially(sample_match):

    assert sample_match.is_finished() is False
