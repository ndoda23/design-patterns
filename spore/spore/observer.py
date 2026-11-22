from typing import Protocol

from spore.creature import Creature
from spore.outcome import Outcome


class SimulationObserver(Protocol):
    def on_evolved(self, role: str, creature: Creature) -> None: ...

    def on_finished(self, outcome: Outcome) -> None: ...


class ConsoleLogger:
    def on_evolved(self, role: str, creature: Creature) -> None:
        body = creature.body
        boosts = ", ".join(str(boost) for boost in body.boosts)
        print(
            f"{role}: position={creature.position}, health={creature.health}, "
            f"stamina={creature.stamina}, power={creature.power}, "
            f"legs={body.legs}, wings={body.wings}, boosts=[{boosts}]"
        )

    def on_finished(self, outcome: Outcome) -> None:
        print(outcome.value)
