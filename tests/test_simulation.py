from observatory.simulation import simulate_run


def test_simulation_is_deterministic():
    kwargs = dict(regime="S1_rewire", topology="WS", n=32, seed_fraction=0.08, beta=0.11, seed=123)
    a = simulate_run(**kwargs)
    b = simulate_run(**kwargs)
    assert a.cascade == b.cascade
    assert a.time_to_cascade == b.time_to_cascade
    assert a.features == b.features


def test_feature_keys_exist():
    r = simulate_run(regime="S0_static", topology="BA", n=32, seed_fraction=0.08, beta=0.11, seed=456)
    assert {"unsafe_fraction", "propagation_rate", "activity_entropy", "avg_clustering", "algebraic_connectivity", "edge_turnover"} <= set(r.features)


def test_grouped_source_split_keeps_configs_disjoint():
    from experiments.synthetic_transfer_sweep import generate_rows, split_source
    rows = generate_rows()
    train, test = split_source(rows)
    def group(r):
        return (r["topology"], r["seed_fraction"], r["beta"])
    assert {group(r) for r in train}.isdisjoint({group(r) for r in test})
