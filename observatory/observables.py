from __future__ import annotations

import math

import networkx as nx
import numpy as np


def unsafe_fraction(state: dict[int, int]) -> float:
    return sum(state.values()) / max(1, len(state))


def propagation_rate(previous: dict[int, int], current: dict[int, int]) -> float:
    return unsafe_fraction(current) - unsafe_fraction(previous)


def activity_entropy(graph: nx.Graph, state: dict[int, int]) -> float:
    weights = []
    for node in graph.nodes():
        active_neighbors = sum(state[nbr] for nbr in graph.neighbors(node))
        weights.append(active_neighbors + state[node])
    total = sum(weights)
    if total == 0:
        return 0.0
    probs = [w / total for w in weights if w > 0]
    return -sum(p * math.log(p) for p in probs)


def algebraic_connectivity(graph: nx.Graph) -> float:
    if graph.number_of_nodes() < 2 or not nx.is_connected(graph):
        return 0.0
    lap = nx.laplacian_matrix(graph).toarray().astype(float)
    vals = np.linalg.eigvalsh(lap)
    vals.sort()
    return float(max(0.0, vals[1]))


def graph_observables(graph: nx.Graph, state: dict[int, int], previous: dict[int, int], turnover: float) -> dict[str, float]:
    return {
        "unsafe_fraction": unsafe_fraction(state),
        "propagation_rate": propagation_rate(previous, state),
        "activity_entropy": activity_entropy(graph, state),
        "avg_clustering": float(nx.average_clustering(graph)),
        "algebraic_connectivity": algebraic_connectivity(graph),
        "edge_turnover": turnover,
    }
