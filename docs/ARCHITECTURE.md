# Architecture

## Pipeline

`topology generator`
→ `synthetic dynamics`
→ `observation at preregistered time`
→ `population/network observables`
→ `prospective eligibility filter`
→ `grouped source holdout`
→ `full predictor + simple baseline`
→ `held-out / cross-regime evaluation`

## Modules

- `observatory/topology.py` — deterministic graph construction.
- `observatory/dynamics.py` — propagation, recovery, rewiring, susceptibility.
- `observatory/simulation.py` — run lifecycle and observation-time capture.
- `observatory/observables.py` — six population/network features.
- `observatory/evaluation.py` — predictor, baseline, metrics, transfer guard.
- `experiments/` — deterministic 864-run sweep and grouped holdout.
- `results/` — canonical machine-readable evidence.

## Leakage-control invariant

Replicates from the same `topology × seed_fraction × beta` configuration must never be split across source development and held-out sets.
