from collections.abc import Sequence
from random import Random
from typing import Protocol

from spore.creature import Creature
from spore.evolution import Evolution, StatRange
from spore.observer import SimulationObserver
from spore.outcome import Outcome

PREDATOR_POSITION = 0
PREY_POSITION = StatRange(0, 1000)


class Phase(Protocol):
    def run(self, predator: Creature, prey: Creature) -> Outcome | None: ...


class Chase:
    def run(self, predator: Creature, prey: Creature) -> Outcome | None:
        while True:
            predator_moved = predator.move()
            prey.move()
            if predator.position >= prey.position:
                return None
            if not predator_moved:
                return Outcome.PREY_ESCAPED


class Fight:
    def run(self, predator: Creature, prey: Creature) -> Outcome:
        while predator.is_alive and prey.is_alive:
            predator.attack(prey)
            prey.attack(predator)
        if prey.is_alive:
            return Outcome.PREY_ESCAPED
        return Outcome.PREY_EATEN


class Simulation:
    def __init__(
        self,
        evolution: Evolution,
        observer: SimulationObserver,
        rng: Random,
        phases: Sequence[Phase],
    ) -> None:
        self._evolution = evolution
        self._observer = observer
        self._rng = rng
        self._phases = phases

    def run(self) -> Outcome:
        predator = self._spawn("Predator", PREDATOR_POSITION)
        prey = self._spawn("Prey", PREY_POSITION.roll(self._rng))
        outcome = self._play(predator, prey)
        self._observer.on_finished(outcome)
        return outcome

    def _spawn(self, role: str, position: int) -> Creature:
        creature = self._evolution.evolve(position)
        self._observer.on_evolved(role, creature)
        return creature

    def _play(self, predator: Creature, prey: Creature) -> Outcome:
        for phase in self._phases:
            outcome = phase.run(predator, prey)
            if outcome is not None:
                return outcome
        raise RuntimeError("Simulation ended without an outcome")
