# Reproducibility contract

1. Install dependencies.
2. Run `python -m pytest -q`.
3. Run `python -m experiments.synthetic_transfer_sweep`.
4. Compare generated CSV/JSON outputs with committed evidence.
5. Keep development and held-out configuration groups disjoint.
6. Do not report transfer-retention ratios when source uplift fails the positive-uplift guard.
7. Record all methodological changes in `CHANGELOG.md`.
