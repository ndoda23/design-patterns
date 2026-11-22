from dataclasses import dataclass

from spore.power import PowerBoost


@dataclass(frozen=True)
class Body:
    legs: int
    wings: int
    boosts: tuple[PowerBoost, ...]

    def boost(self, power: int) -> int:
        for boost in self.boosts:
            power = boost.apply(power)
        return power
