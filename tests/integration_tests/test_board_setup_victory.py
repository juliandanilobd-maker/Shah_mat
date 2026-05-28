from app.domain.board.board import Board
from app.domain.board.position import Position
from app.domain.units.lancer import Lancer
from app.domain.units.heavy_cavalry import HeavyCavalry
from app.domain.units.light_cavalry import LightCavalry
from app.domain.units.king import King
from app.application.services.victory_service import VictoryService


class TestSetupInitialState:

    def setup_method(self):
        self.board = Board()
        self.board.setup_initial_state()

    # comprobar si el rey inicia en la casilla correcta
    def test_king_player_one_in_correct_position(self):
        piece = self.board.get_piece(Position(0, 4))
        assert isinstance(piece, King)
        assert piece.owner == "Jugador 1"

    # comprobar si el otro rey esta en su casilla
    def test_king_player_two_in_correct_position(self):
        piece = self.board.get_piece(Position(9, 4))
        assert isinstance(piece, King)
        assert piece.owner == "Jugador 2"

    # comprobar si caballeria ligera inicia en su casilla correcta
    def test_lightcavalry_player_one_in_correct_position(self):
        for col in [0, 8]:
            piece = self.board.get_piece(Position(0, col))
            assert isinstance(piece, LightCavalry)
            assert piece.owner == "Jugador 1"

    # comprobar si la caballeria pesada inicia en su casilla correcta
    def test_heavycavalry_player_one_in_correct_position(self):
        for col in [2, 6]:
            piece = self.board.get_piece(Position(0, col))
            assert isinstance(piece, HeavyCavalry)
            assert piece.owner == "Jugador 1"

    # comprobar las posiciones iniciales de los lanceros jugador 1
    def test_lancer_player_one_in_correct_position(self):
        for col in range(0, 10, 2):
            piece = self.board.get_piece(Position(1, col))
            assert isinstance(piece, Lancer)
            assert piece.owner == "Jugador 1"

    # comprobar las posiciones iniciales de los lanceros jugador 2
    def test_lightcavalry_player_two_in_correct_position(self):
        for col in range(0, 10, 2):
            piece = self.board.get_piece(Position(8, col))
            assert isinstance(piece, Lancer)
            assert piece.owner == "Jugador 2"

    # comprobar que la zona central inicie vacia
    def test_central_zone_empty(self):
        for row in range(2, 8):
            for col in range(10):
                assert self.board.is_empty(Position(row, col))

    # determinar que ambos jugadores inician con 10 piezas
    def test_total_pieces_player_one(self):
        pieces = [p for _, p in self.board.get_all_pieces() if p.owner == "Jugador 1"]
        assert len(pieces) == 10

    def test_total_pieces_player_two(self):
        pieces = [p for _, p in self.board.get_all_pieces() if p.owner == "Jugador 2"]
        assert len(pieces) == 10


class TestVictoryService:

    def setup_method(self):
        self.board = Board()
        self.board.setup_initial_state()
        self.victory = VictoryService()

    # no se inicia con victoria
    def test_no_intial_victory(self):
        assert self.victory.check_victory(self.board) is None

    # partida no se termina al inicio
    def test_no_initialize_with_game_over(self):
        assert self.victory.is_game_over(self.board) is False

    # comprobar si se genera la victoria si se dan las condiciones
    def test_player_two_wins_if_player_one_king_dies(self):
        king1 = self.board.get_piece(Position(0, 4))
        king1.take_attack(99)
        king1.take_attack(99)
        king1.take_attack(99)
        king1.take_attack(99)
        assert king1.is_alive() is False
        assert self.victory.check_victory(self.board) == "Jugador 2"

    def test_player_one_wins_if_player_two_king_dies(self):
        king2 = self.board.get_piece(Position(9, 4))
        king2.take_attack(99)
        king2.take_attack(99)
        king2.take_attack(99)
        king2.take_attack(99)
        assert king2.is_alive() is False
        assert self.victory.check_victory(self.board) == "Jugador 1"

    def test_game_over_when_king_dies(self):
        king1 = self.board.get_piece(Position(0, 4))
        king1.take_attack(99)
        king1.take_attack(99)
        king1.take_attack(99)
        king1.take_attack(99)
        assert self.victory.is_game_over(self.board) is True

    def test_no_victory_if_both_kings_alive(self):
        assert self.victory.check_victory(self.board) is None
