from enum import Enum
from typing import Protocol


class PowerBoost(Protocol):
    def apply(self, power: int) -> int: ...


class Claws(Enum):
    NONE = 1
    SMALL = 2
    MEDIUM = 3
    BIG = 4

    def apply(self, power: int) -> int:
        return power * self.value


class Teeth(Enum):
    NONE = 0
    DULL = 3
    SHARP = 6
    RAZOR = 9

    def apply(self, power: int) -> int:
        return power + self.value
