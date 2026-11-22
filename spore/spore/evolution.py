from dataclasses import dataclass
from random import Random
from typing import Protocol

from spore.body import Body
from spore.creature import Creature
from spore.power import Claws, Teeth


@dataclass(frozen=True)
class StatRange:
    low: int
    high: int

    def roll(self, rng: Random) -> int:
        return rng.randint(self.low, self.high)


HEALTH = StatRange(50, 150)
STAMINA = StatRange(0, 1000)
POWER = StatRange(1, 10)
LEGS = StatRange(0, 4)
WINGS = StatRange(0, 4)


class Evolution(Protocol):
    def evolve(self, position: int) -> Creature: ...


class RandomEvolution:
    def __init__(self, rng: Random) -> None:
        self._rng = rng

    def evolve(self, position: int) -> Creature:
        return Creature(
            body=self._evolve_body(),
            position=position,
            health=HEALTH.roll(self._rng),
            stamina=STAMINA.roll(self._rng),
            power=POWER.roll(self._rng),
        )

    def _evolve_body(self) -> Body:
        claws = self._rng.choice(list(Claws))
        teeth = self._rng.choice(list(Teeth))
        return Body(
            legs=LEGS.roll(self._rng),
            wings=WINGS.roll(self._rng),
            boosts=(claws, teeth),
        )
