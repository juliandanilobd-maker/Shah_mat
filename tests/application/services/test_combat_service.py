from app.application.services.combat_service import CombatService
from app.domain.units.health_state import HealthState


# Se crea una clase FakePiece para simular interacciones de combate y defensa
class FakePiece:

    def __init__(self, owner="jugador1", movement_range=3, defense=2, attack_value=5):
        self.owner = owner
        self.movement_range = movement_range
        self.defense = defense
        self.attack_value = attack_value
        self.state = HealthState.SHIELD

    def recieve_attack(self, attack: int) -> bool:
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


class TestCombatService:

    def setup_method(self):
        self.combat = CombatService()

    # Un ataque exitoso reduce la vida
    def test_attack_successful(self):
        attacker = FakePiece(attack_value=5)
        defender = FakePiece(defense=2)
        self.combat.attack(attacker, defender)
        assert defender.state == HealthState.DAMAGED

    # Un ataque bloqueado no reduce la vida
    def test_attack_blocked(self):
        attacker = FakePiece(attack_value=2)
        defender = FakePiece(defense=2)
        self.combat.attack(attacker, defender)
        assert defender.state == HealthState.SHIELD

    # Un ataque menor a la defensa tampoco cambia el estado
    def test_attack_failed(self):
        attacker = FakePiece(attack_value=2)
        defender = FakePiece(defense=3)
        self.combat.attack(attacker, defender)
        assert defender.state == HealthState.SHIELD

    # 3 ataques destruyen la pieza
    def test_attack_destroy_piece(self):
        attacker = FakePiece(attack_value=10)
        defender = FakePiece(defense=2)
        self.combat.attack(attacker, defender)
        self.combat.attack(attacker, defender)
        self.combat.attack(attacker, defender)
        assert defender.state == HealthState.DEAD
