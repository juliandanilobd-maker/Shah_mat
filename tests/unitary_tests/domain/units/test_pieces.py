from app.domain.units.lancer import Lancer
from app.domain.units.heavy_cavalry import HeavyCavalry
from app.domain.units.light_cavalry import LightCavalry
from app.domain.units.king import King
from app.domain.units.health_state import HealthState
from app.domain.board.position import Position
from app.domain.board.move import Move


def move(r1, c1, r2, c2):
    return Move(Position(r1, c1), Position(r2, c2))


class TestStats:

    # creamos las funciones que testean las stats de las piezas
    def test_lancer_stats(self):
        p = Lancer("p1")
        assert p.attack_value == 1
        assert p.defense == 1
        assert p.movement_range == 1

    def test_light_cavalry(self):
        p = LightCavalry("p1")
        assert p.attack_value == 2
        assert p.defense == 2
        assert p.movement_range == 3

    def test_heavy_cavalry(self):
        p = HeavyCavalry("p1")
        assert p.attack_value == 2
        assert p.defense == 2
        assert p.movement_range == 2

    def test_king(self):
        p = King("p1")
        assert p.attack_value == 1
        assert p.defense == 2
        assert p.movement_range == 1

    # Determina que se inica con estado shield
    def initial_state_shield(self):
        for cls in [Lancer, LightCavalry, HeavyCavalry, King]:
            assert cls("p1").state == HealthState.SHIELD


class TestModifiers:

    # funciones para probar que la funcion modifier suma correctamente al valor base
    # y no sobreescribe el valor base
    def test_defense_modifier(self):
        p = HeavyCavalry("p1")
        p._defense_modifier = 1
        assert p.defense == 3

    def test_attack_modifier(self):
        p = LightCavalry("p1")
        p._attack_modifier = 2
        assert p.attack_value == 4

    def test_base_no_modified_for_the_modifier(self):
        p = King("p1")
        p._defense_modifier = 3
        assert p._base_defense == 2
        assert p.defense == 5


class TestLancer:

    # Se comprueba que Lancer se mueve en sentido horizontal y vertical, no en diagonal
    def test_move_up(self):
        assert Lancer("p1").can_move(move(1, 0, 0, 0)) is True

    def test_move_down(self):
        assert Lancer("p1").can_move(move(0, 0, 1, 0)) is True

    def test_move_right(self):
        assert Lancer("p1").can_move(move(0, 0, 0, 1)) is True

    def test_move_left(self):
        assert Lancer("p1").can_move(move(0, 1, 0, 0)) is True

    def test_no_move_diagonal(self):
        assert Lancer("p1").can_move(move(0, 0, 1, 1)) is False

    def test_no_move_out_of_range(self):
        assert Lancer("p1").can_move(move(0, 0, 0, 2)) is False

    def test_no_move_null_move(self):
        assert Lancer("p1").can_move(move(0, 0, 0, 0)) is False


class TestLightCavalry:

    # se comprueba los movimientos correctos de LightCavalry
    def test_move_cardinal(self):
        assert LightCavalry("p1").can_move(move(0, 0, 0, 3)) is True

    def test_move_diagonal(self):
        assert LightCavalry("p1").can_move(move(0, 0, 2, 1)) is True

    def test_no_move_out_of_range(self):
        assert LightCavalry("p1").can_move(move(0, 0, 0, 4)) is False

    def test_no_move_null_move(self):
        assert LightCavalry("p1").can_move(move(2, 2, 2, 2)) is False


class TestHeavyCavalry:

    # se comprueba los movimientos correctos de HeavyCavalry
    def test_move_cardinal(self):
        assert HeavyCavalry("p1").can_move(move(0, 0, 0, 2)) is True

    def test_move_diagonal(self):
        assert HeavyCavalry("p1").can_move(move(0, 0, 1, 1)) is True

    def test_no_move_out_of_range(self):
        assert HeavyCavalry("p1").can_move(move(0, 0, 0, 3)) is False

    def test_no_move_null_move(self):
        assert HeavyCavalry("p1").can_move(move(1, 1, 1, 1)) is False


class TestKing:

    # se comprueba los movimientos correctos de King
    def test_move_cardinal(self):
        assert King("p1").can_move(move(4, 4, 4, 5)) is True

    def test_move_diagonal(self):
        assert King("p1").can_move(move(4, 5, 5, 5)) is True

    def test_no_move_out_of_range(self):
        assert King("p1").can_move(move(4, 4, 4, 6)) is False

    def test_no_move_null_move(self):
        assert King("p1").can_move(move(4, 4, 4, 4)) is False
