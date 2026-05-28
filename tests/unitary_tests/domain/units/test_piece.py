from app.domain.units.piece import Piece
from app.domain.units.health_state import HealthState
from app.domain.board.move import Move


# Se establece una clase minima para testear la clase Piece
class ConcretePiece(Piece):

    def can_move(self, move) -> bool:
        if move is None:
            return False
        return move.distance() <= self.movement_range


class TestHealthState:

    # Comprobar si los estados de salud se enumeran de forma correcta
    def test_HealthState_values(self):
        assert HealthState.SHIELD.value == 1
        assert HealthState.DAMAGED.value == 2
        assert HealthState.CRITICAL.value == 3
        assert HealthState.DEAD.value == 4


class TestPiece:

    def setup_method(self):

        self.piece = ConcretePiece(
            "jugador1", movement_range=3, defense=2, attack_value=5
        )

    # Se inicia la pieza con el primer estado de salud
    def test_initial_health_state(self):
        assert self.piece.state == HealthState.SHIELD

    # Se inicia con pieza viva
    def test_alive_piece(self):
        assert self.piece.is_alive() is True

    # Ataque igual a defensa, no hace daño
    def test_attack_blocked(self):
        result = self.piece.take_attack(2)
        assert result is False
        assert self.piece.state == HealthState.SHIELD

    # Ataque menor a defensa, no hace daño
    def test_attacked_less_than_defense(self):
        result = self.piece.take_attack(1)
        assert result is False
        assert self.piece.state == HealthState.SHIELD

    # Ataque superior a defensa hace daño
    def test_attack_greater_than_defense(self):
        result = self.piece.take_attack(3)
        assert result is True
        assert self.piece.state == HealthState.DAMAGED

    # Dos ataques dejan en estado Critical
    def test_attack_twice(self):
        self.piece.take_attack(3)
        self.piece.take_attack(3)
        assert self.piece.state == HealthState.CRITICAL

    # Tres ataques derriban la pieza
    def test_dead_piece(self):
        self.piece.take_attack(3)
        self.piece.take_attack(3)
        self.piece.take_attack(3)
        assert self.piece.state == HealthState.DEAD
        assert self.piece.is_alive() is False

    # Una pieza derribada, no puede recibir downgrades
    def test_dead_piece_takes_no_attack(self):
        for _ in range(5):
            self.piece.take_attack(99)
        assert self.piece.state == HealthState.DEAD

    # Comprobar que existe attack_value
    def test_attack_value_exists(self):
        assert hasattr(self.piece, "attack_value")
        assert self.piece.attack_value == 5

    # Comprobar que la pieza se puede mover
    def text_can_move_in_movement_range(self):
        from app.domain.board.position import Position

        move = Move(Position(0, 0), Position(0, 3))
        assert self.piece.can_move(move) is True

    # No puede moverse fuera de su rango de movimiento
    def text_cant_move_out_of_movement_range(self):
        from app.domain.board.position import Position

        move = Move(Position(0, 0), Position(0, 5))
        assert self.piece.can_move(move) is False
