from app.application.services.movement_service import MovementService
from app.domain.board.board import Board
from app.domain.board.move import Move
from app.domain.board.position import Position
from app.domain.units.health_state import HealthState


# Se crea una clase FakePiece para simular interacciones de combate y defensa
class FakePiece:

    def __init__(self, owner="jugador1", movement_range=3, defense=2, attack_value=5):
        self.owner = owner
        self.movement_range = movement_range
        self.defense = defense
        self.attack_value = attack_value
        self.state = HealthState.SHIELD

    def take_attack(self, attack: int) -> bool:
        if attack <= self.defense:
            return False

        if self.state == HealthState.SHIELD:
            self.state = HealthState.DAMAGED

        elif self.state == HealthState.DAMAGED:
            self.state = HealthState.CRITICAL

        elif self.state == HealthState.CRITICAL:
            self.state = HealthState.DEAD

        return True

    def is_alive(self):
        return self.state != HealthState.DEAD


class TestMovementService:

    def setup_method(self):
        self.service = MovementService()
        self.board = Board()
        self.piece = FakePiece(owner="jugador1", movement_range=3)

    # Funcion para colocar la pieza creada en una casilla
    def place_piece(self, row, col):
        position = Position(row, col)
        self.board.place_piece(position, self.piece)
        return position

    # Comprobar si movement_service comprueba las casillas validas
    def test_valid_move(self):
        origin = self.place_piece(0, 0)
        move = Move(origin, Position(0, 2))
        assert self.service.validate_move(self.board, move, "jugador1") is True

    # Comrpobar si movement_service comprueba casillas al limite del rango de movimiento
    def test_valid_move_at_limit_range(self):
        origin = self.place_piece(0, 0)
        move = Move(origin, Position(0, 3))
        assert self.service.validate_move(self.board, move, "jugador1") is True

    # Verificar si movement_service comprueba si no existe pieza colocada en origen
    def test_no_piece_in_origin(self):
        move = Move(Position(5, 5), Position(5, 6))
        assert self.service.validate_move(self.board, move, "jugador1") is False

    # Verificar si movement_service comprueba que la pieza es de otro jugador
    def test_no_current_player_piece(self):
        origin = self.place_piece(2, 2)
        move = Move(origin, Position(2, 3))
        assert self.service.validate_move(self.board, move, "jugador2") is False

    # movement_service comprueba si la casilla esta fuera de limite
    def test_out_of_bounds_grid(self):
        origin = Position(0, 0)
        move = Move(origin, Position(0, 99))
        assert self.service.validate_move(self.board, move, "jugador1") is False

    # movement_service comprueba el maximo rango de movimiento
    def test_movement_range(self):
        origin = self.place_piece(0, 0)
        move = Move(origin, Position(0, 5))
        assert self.service.validate_move(self.board, move, "jugador1") is False
