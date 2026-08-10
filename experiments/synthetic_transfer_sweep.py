from __future__ import annotations

import csv
import json
from pathlib import Path

from observatory.evaluation import BASELINE_FEATURES, FEATURES, evaluate, fit_predictor, transfer_retention
from observatory.simulation import simulate_run


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
REGIMES = ["S0_static", "S1_rewire", "S2_heterogeneous"]
TOPOLOGIES = ["ER", "WS", "BA"]


def generate_rows():
    rows = []
    run_id = 0
    for regime_idx, regime in enumerate(REGIMES):
        for topology_idx, topology in enumerate(TOPOLOGIES):
            for seed_fraction in [0.01, 0.03, 0.05]:
                for beta in [0.03, 0.05, 0.07, 0.11]:
                    for replicate in range(8):
                        seed = 100000 * regime_idx + 10000 * topology_idx + 1000 * int(seed_fraction * 100) + 100 * int(beta * 100) + replicate
                        result = simulate_run(
                            regime=regime,
                            topology=topology,
                            n=64,
                            seed_fraction=seed_fraction,
                            beta=beta,
                            seed=seed,
                        )
                        row = {
                            "run_id": run_id,
                            "regime": regime,
                            "topology": topology,
                            "n": result.n,
                            "seed_fraction": seed_fraction,
                            "beta": beta,
                            "seed": seed,
                            "cascade": result.cascade,
                            "time_to_cascade": "" if result.time_to_cascade is None else result.time_to_cascade,
                            "forecast_eligible": int(result.time_to_cascade is None or result.time_to_cascade > 5),
                            "future_cascade": int(result.time_to_cascade is not None and result.time_to_cascade > 5),
                            **result.features,
                        }
                        rows.append(row)
                        run_id += 1
    return rows


def split_source(rows):
    from sklearn.model_selection import GroupShuffleSplit

    source = [r for r in rows if r["regime"] == "S0_static" and r["forecast_eligible"] == 1]
    groups = [f"{r['topology']}|{r['seed_fraction']:.3f}|{r['beta']:.3f}" for r in source]
    splitter = GroupShuffleSplit(n_splits=1, test_size=0.25, random_state=0)
    train_idx, test_idx = next(
        splitter.split(source, [r["future_cascade"] for r in source], groups)
    )
    train = [source[i] for i in train_idx]
    test = [source[i] for i in test_idx]
    if len({r["future_cascade"] for r in train}) < 2 or len({r["future_cascade"] for r in test}) < 2:
        raise ValueError("grouped split must contain both cascade classes in train and test")
    return train, test


def main():
    RESULTS.mkdir(exist_ok=True)
    rows = generate_rows()

    csv_path = RESULTS / "synthetic_transfer_runs.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    train, source_test = split_source(rows)
    full_model = fit_predictor(train, FEATURES)
    baseline_model = fit_predictor(train, BASELINE_FEATURES)

    evaluations = {}
    for regime in REGIMES:
        eval_rows = source_test if regime == "S0_static" else [
            r for r in rows if r["regime"] == regime and r["forecast_eligible"] == 1
        ]
        evaluations[regime] = {
            "full": evaluate(full_model, eval_rows, FEATURES),
            "baseline_unsafe_fraction": evaluate(baseline_model, eval_rows, BASELINE_FEATURES),
        }

    source_full = evaluations["S0_static"]["full"]["auroc"]
    source_base = evaluations["S0_static"]["baseline_unsafe_fraction"]["auroc"]
    retention = {}
    absolute_uplift = {}
    for regime in REGIMES:
        target_full = evaluations[regime]["full"]["auroc"]
        target_base = evaluations[regime]["baseline_unsafe_fraction"]["auroc"]
        absolute_uplift[regime] = target_full - target_base
        retention[regime] = transfer_retention(
            source_full,
            source_base,
            target_full,
            target_base,
        )

    summary = {
        "prototype_status": "PIPELINE_VALIDATED",
        "scientific_hypothesis": "NOT_ESTABLISHED",
        "note": "All regimes are synthetic instrumentation regimes; none are LLM/frontier-agent fidelity levels.",
        "feature_names": FEATURES,
        "baseline_features": BASELINE_FEATURES,
        "total_runs": len(rows),
        "forecast_eligible_runs": sum(r["forecast_eligible"] for r in rows),
        "evaluation": evaluations,
        "absolute_uplift_auroc": absolute_uplift,
        "transfer_retention_auroc": retention,
        "transfer_retention_min_source_uplift": 0.01,
    }
    (RESULTS / "synthetic_transfer_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print("Agent Network Transition Observatory — Synthetic Transfer Sweep 001")
    print(f"Runs: {len(rows)}")
    for regime, pair in evaluations.items():
        full = pair["full"]
        base = pair["baseline_unsafe_fraction"]
        print(
            f"{regime}: full_AUROC={full['auroc']:.3f}, baseline_AUROC={base['auroc']:.3f}, "
            f"full_AUPRC={full['auprc']:.3f}, prevalence={full['prevalence']:.3f}, n={full['n']}"
        )
    for regime, value in retention.items():
        if value is None:
            print(f"transfer retention {regime}: undefined")
        else:
            print(f"transfer retention {regime}: {value:.3f}")
    print("STATUS: PIPELINE_VALIDATED")
    print("SCIENTIFIC_HYPOTHESIS: NOT_ESTABLISHED")


if __name__ == "__main__":
    main()
