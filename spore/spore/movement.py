from collections.abc import Callable, Sequence
from dataclasses import dataclass
from typing import Protocol

from spore.body import Body


@dataclass(frozen=True)
class Movement:
    name: str
    required_stamina: int
    stamina_cost: int
    speed: int
    is_supported_by: Callable[[Body], bool]

    def is_possible(self, body: Body, stamina: int) -> bool:
        enough_stamina = stamina >= max(self.required_stamina, self.stamina_cost)
        return enough_stamina and self.is_supported_by(body)


MOVEMENTS: tuple[Movement, ...] = (
    Movement("Crawl", 0, 1, 1, lambda body: True),
    Movement("Hop", 20, 2, 3, lambda body: body.legs >= 1),
    Movement("Walk", 40, 2, 4, lambda body: body.legs >= 2),
    Movement("Run", 60, 4, 6, lambda body: body.legs >= 2),
    Movement("Fly", 80, 4, 8, lambda body: body.wings >= 2),
)


class MovementStrategy(Protocol):
    def choose(self, options: Sequence[Movement]) -> Movement | None: ...


class FastestMovement:
    def choose(self, options: Sequence[Movement]) -> Movement | None:
        return max(options, key=lambda movement: movement.speed, default=None)
