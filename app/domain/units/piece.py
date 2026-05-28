from abc import ABC, abstractmethod
from app.domain.board.move import Move
from app.domain.units.health_state import HealthState


# Aplicamos principios de herencia, creamos una clase Piece, que será el molde sobre el
# cual las piezas especificas del juego escribiran sus atributos
class Piece(ABC):

    def __init__(
        self, owner: str, movement_range: int, defense: int, attack_value: int
    ):

        self.owner = owner
        self.movement_range = movement_range
        self._base_defense = defense
        self._base_attack = attack_value
        self._defense_modifier = 0
        self._attack_modifier = 0
        self.state = HealthState.SHIELD

    # Creamos una funcion que va a ser atributo base, en este caso defensa base
    @property
    def defense(self) -> int:
        return self._base_defense + self._defense_modifier

    # Creamos una funcion que se va a ser atributo base, en este caso ataque base
    @property
    def attack_value(self) -> int:
        return self._base_attack + self._attack_modifier

    # Este decorador indica que las clases herederas están obligadas a escribir
    # su versión de este metodo
    # Creamos la función que define si la pieza puede realizar el movimiento

    @abstractmethod
    def can_move(self, move: Move) -> bool:
        pass

    # Creamos la función que reduce un estado de vida
    def _downgrade_state(self):
        if self.state == HealthState.SHIELD:
            self.state = HealthState.DAMAGED

        elif self.state == HealthState.DAMAGED:
            self.state = HealthState.CRITICAL

        elif self.state == HealthState.CRITICAL:
            self.state = HealthState.DEAD

    # Creamos la función que reduce un estado de vida de la pieza
    def take_attack(self, attack: int) -> bool:

        if attack <= self.defense:
            return False

        self._downgrade_state()
        return True

    # Creamos la función que determina si la pieza sigue con vida
    def is_alive(self) -> bool:

        return self.state != HealthState.DEAD
