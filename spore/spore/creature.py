from collections.abc import Sequence
from dataclasses import dataclass, field

from spore.body import Body
from spore.movement import MOVEMENTS, FastestMovement, Movement, MovementStrategy


@dataclass
class Creature:
    body: Body
    position: int
    health: int
    stamina: int
    power: int
    strategy: MovementStrategy = field(default_factory=FastestMovement)
    movements: Sequence[Movement] = MOVEMENTS

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    @property
    def attack_power(self) -> int:
        return self.body.boost(self.power)

    def move(self) -> bool:
        movement = self.strategy.choose(self._possible_movements())
        if movement is None:
            return False
        self.stamina -= movement.stamina_cost
        self.position += movement.speed
        return True

    def attack(self, other: "Creature") -> None:
        other.take_damage(self.attack_power)

    def take_damage(self, damage: int) -> None:
        self.health = max(0, self.health - damage)

    def _possible_movements(self) -> list[Movement]:
        return [m for m in self.movements if m.is_possible(self.body, self.stamina)]
