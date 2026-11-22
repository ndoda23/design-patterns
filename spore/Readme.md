# Spore: Predator vs Prey Simulation

Assignment 1 for the Design Patterns course. Inspired by the game
[Spore](https://www.spore.com/), where creatures evolve body parts
such as legs, wings, claws and teeth.

## What it does

The world is an infinite ray that starts at position `0`. Each simulation has three phases:

1. **Evolution**: a random predator appears at position `0` and a random prey somewhere in `0–1000`. Both are logged once.
2. **Chase**: both creatures move and spend stamina, always using the fastest movement available.
   - Predator runs out of stamina → `Pray ran into infinity`
   - Predator catches the prey → fight
3. **Fight**: both attack each round (no stamina is used).
   - Predator dies → `Pray ran into infinity`
   - Prey dies → `Some R-rated things have happened`

The program runs 100 simulations.

### Rules

| Movement | Needs             | Min stamina | Cost | Speed |
|----------|-------------------|-------------|------|-------|
| Crawl    | nothing           | 0           | 1    | 1     |
| Hop      | 1+ legs           | 20          | 2    | 3     |
| Walk     | 2+ legs           | 40          | 2    | 4     |
| Run      | 2+ legs           | 60          | 4    | 6     |
| Fly      | 2+ wings          | 80          | 4    | 8     |

- **Claws** multiply attack power: small ×2, medium ×3, big ×4
- **Teeth** add attack power: +3, +6, +9

## Run

Requires Python 3.13+.

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows (Mac/Linux: source .venv/bin/activate)
pip install ruff mypy
python main.py
```

Lint and type-check:

```bash
ruff format .
ruff check .
mypy .
```

## Project structure

```
spore/
├── power.py        # Claws, Teeth (attack power boosts)
├── body.py         # legs, wings, boosts
├── movement.py     # movement table + movement strategies
├── creature.py     # creature state, move(), attack()
├── evolution.py    # random creature creation
├── observer.py     # logging
├── outcome.py      # simulation results
└── simulation.py   # Chase and Fight phases, simulation runner
main.py             # runs 100 simulations
```

## Design patterns

- **Strategy**: `MovementStrategy` decides how a creature moves (greedy by default), and `PowerBoost` decides how claws and teeth change attack power. Behavior can be swapped without touching `Creature`.
- **Factory**: `Evolution` creates creatures, so the simulation does not depend on how they are built.
- **Observer**: `SimulationObserver` handles
