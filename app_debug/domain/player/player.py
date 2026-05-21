from abc import ABC, abstractmethod
from typing import Any


class Player(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_action(self) -> dict[str, Any]:
        pass
