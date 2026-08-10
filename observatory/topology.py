from __future__ import annotations

import networkx as nx
import random


def make_graph(kind: str, n: int, seed: int) -> nx.Graph:
    if kind == "ER":
        return nx.erdos_renyi_graph(n, 0.08, seed=seed)
    if kind == "WS":
        return nx.watts_strogatz_graph(n, k=6, p=0.12, seed=seed)
    if kind == "BA":
        return nx.barabasi_albert_graph(n, m=3, seed=seed)
    raise ValueError(f"unknown topology: {kind}")


def rewire_fraction(graph: nx.Graph, fraction: float, rng: random.Random) -> tuple[nx.Graph, float]:
    if fraction <= 0 or graph.number_of_edges() == 0:
        return graph.copy(), 0.0
    g = graph.copy()
    edges = list(g.edges())
    count = max(1, int(round(len(edges) * fraction)))
    chosen = rng.sample(edges, min(count, len(edges)))
    removed = 0
    added = 0
    for u, v in chosen:
        if g.has_edge(u, v):
            g.remove_edge(u, v)
            removed += 1
        for _ in range(20):
            a = rng.randrange(g.number_of_nodes())
            b = rng.randrange(g.number_of_nodes())
            if a != b and not g.has_edge(a, b):
                g.add_edge(a, b)
                added += 1
                break
    turnover = (removed + added) / max(1, 2 * len(edges))
    return g, turnover
