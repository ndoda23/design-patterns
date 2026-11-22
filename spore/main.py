from random import Random

from spore.evolution import RandomEvolution
from spore.observer import ConsoleLogger
from spore.simulation import Chase, Fight, Simulation

SIMULATION_COUNT = 100


def main() -> None:
    rng = Random()
    simulation = Simulation(
        evolution=RandomEvolution(rng),
        observer=ConsoleLogger(),
        rng=rng,
        phases=(Chase(), Fight()),
    )
    for number in range(1, SIMULATION_COUNT + 1):
        print(f"--- Simulation {number} ---")
        simulation.run()


if __name__ == "__main__":
    main()
