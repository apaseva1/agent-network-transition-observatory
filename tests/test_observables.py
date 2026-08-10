import networkx as nx

from observatory.observables import algebraic_connectivity, unsafe_fraction


def test_unsafe_fraction():
    assert unsafe_fraction({0: 1, 1: 0, 2: 1, 3: 0}) == 0.5


def test_algebraic_connectivity_path_positive():
    g = nx.path_graph(5)
    assert algebraic_connectivity(g) > 0
