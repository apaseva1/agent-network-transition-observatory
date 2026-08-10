from __future__ import annotations

import random
from dataclasses import dataclass

from .dynamics import initial_state, step, susceptibility
from .observables import graph_observables, unsafe_fraction
from .topology import make_graph


@dataclass(frozen=True)
class RunResult:
    regime: str
    topology: str
    n: int
    seed_fraction: float
    beta: float
    seed: int
    cascade: int
    time_to_cascade: int | None
    features: dict[str, float]


def simulate_run(
    *,
    regime: str,
    topology: str,
    n: int,
    seed_fraction: float,
    beta: float,
    seed: int,
    observation_time: int = 5,
    horizon: int = 24,
    cascade_threshold: float = 0.50,
) -> RunResult:
    rng = random.Random(seed)
    graph = make_graph(topology, n, seed)
    # Avoid disconnected ER edge cases while keeping reproducibility.
    if topology == "ER" and graph.number_of_edges() == 0:
        graph = make_graph("WS", n, seed)
    state = initial_state(graph, seed_fraction, rng)
    susc = susceptibility(graph, regime, rng)
    previous = dict(state)
    features = None
    time_to_cascade = None

    for t in range(1, horizon + 1):
        result = step(graph, state, beta, recovery=0.01, regime=regime, susceptibility_map=susc, rng=rng)
        graph, state = result.graph, result.state
        if t == observation_time:
            features = graph_observables(graph, state, previous, result.turnover)
        if time_to_cascade is None and unsafe_fraction(state) >= cascade_threshold:
            time_to_cascade = t
        previous = dict(state)

    if features is None:
        raise RuntimeError("observation_time must be within horizon")

    return RunResult(
        regime=regime,
        topology=topology,
        n=n,
        seed_fraction=seed_fraction,
        beta=beta,
        seed=seed,
        cascade=int(time_to_cascade is not None),
        time_to_cascade=time_to_cascade,
        features=features,
    )
