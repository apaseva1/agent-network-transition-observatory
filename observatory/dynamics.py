from __future__ import annotations

import math
import random
from dataclasses import dataclass

import networkx as nx

from .topology import rewire_fraction


@dataclass
class StepResult:
    graph: nx.Graph
    state: dict[int, int]
    turnover: float


def initial_state(graph: nx.Graph, seed_fraction: float, rng: random.Random) -> dict[int, int]:
    nodes = list(graph.nodes())
    k = max(1, int(round(len(nodes) * seed_fraction)))
    unsafe = set(rng.sample(nodes, min(k, len(nodes))))
    return {node: int(node in unsafe) for node in nodes}


def susceptibility(graph: nx.Graph, regime: str, rng: random.Random) -> dict[int, float]:
    if regime == "S2_heterogeneous":
        # Deterministic given RNG seed; bounded heterogeneity around 1.0.
        return {node: rng.uniform(0.55, 1.45) for node in graph.nodes()}
    return {node: 1.0 for node in graph.nodes()}


def step(
    graph: nx.Graph,
    state: dict[int, int],
    beta: float,
    recovery: float,
    regime: str,
    susceptibility_map: dict[int, float],
    rng: random.Random,
) -> StepResult:
    turnover = 0.0
    g = graph
    if regime == "S1_rewire":
        g, turnover = rewire_fraction(graph, 0.04, rng)

    new_state = dict(state)
    for node in g.nodes():
        if state[node] == 1:
            if rng.random() < recovery:
                new_state[node] = 0
            continue

        unsafe_neighbors = sum(state[nbr] for nbr in g.neighbors(node))
        if unsafe_neighbors == 0:
            continue
        effective_beta = min(0.95, beta * susceptibility_map[node])
        p = 1.0 - (1.0 - effective_beta) ** unsafe_neighbors
        if rng.random() < p:
            new_state[node] = 1

    return StepResult(g, new_state, turnover)
