import pytest

from app.application.manager.turn_manager import TurnManager


@pytest.fixture
def pvp_manager():
    manager = TurnManager()
    manager.setup_players("PVP")
    return manager


class TestTurnManager:

    # Verifica si se crean los dos jugadores
    def test_setup_creates_two_players(self, pvp_manager):
        assert len(pvp_manager.players) == 2

    # Verifica si los jugadores se crean con los nombres correctos
    def test_name_players(self, pvp_manager):
        assert pvp_manager.players[0].name == "Jugador 1"
        assert pvp_manager.players[1].name == "Jugador 2"

    # Verifica que el priemr turno sea para el jugador 1
    def test_player_one_first_turn(self, pvp_manager):
        assert pvp_manager.get_current_player().name == "Jugador 1"

    # Verifica que el siguiente turno es para el jugador 2
    def test_next_turn_player_two(self, pvp_manager):
        pvp_manager.next_turn()
        assert pvp_manager.get_current_player().name == "Jugador 2"

    # El siguiente turno retorna al jugador 1
    def test_next_turn_back_to_player_one(self, pvp_manager):
        pvp_manager.next_turn()
        pvp_manager.next_turn()
        assert pvp_manager.get_current_player().name == "Jugador 1"

    # El cambio de turnos alterna entre jugadores
    def test_turn_alternates_between_players(self, pvp_manager):
        names = []
        for _ in range(6):
            names.append(pvp_manager.get_current_player().name)
            pvp_manager.next_turn()
        assert names == [
            "Jugador 1",
            "Jugador 2",
            "Jugador 1",
            "Jugador 2",
            "Jugador 1",
            "Jugador 2",
        ]

    # Se inicia el conteo de turnos desde 0
    def test_turn_counter_initialize_zero(self, pvp_manager):
        assert pvp_manager.current_index == 0

    # Se obtiene el primer turno con numero 1
    def test_first_turn_is_one(self, pvp_manager):
        assert pvp_manager.get_turn_number() == 1

    # Segundo turno es el numero 2
    def test_second_turn_is_two(self, pvp_manager):

        pvp_manager.next_turn()
        assert pvp_manager.get_turn_number() == 2
