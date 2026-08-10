# R1 Audit — Agent Network Transition Observatory — Hardened

## Gate results
- Unit tests: PASS (8/8)
- Deterministic seeded simulator: PASS
- Synthetic transfer sweep: PASS
- Forecast eligibility excludes already-cascaded runs: PASS
- Grouped configuration holdout: PASS
- Simple current-unsafe-fraction baseline: PRESENT
- Dynamic-topology regime: PRESENT
- Heterogeneous-susceptibility regime: PRESENT
- Claim boundary: PRESENT
- Falsification contract: PRESENT
- Real generated outputs: PRESENT

## Current generated prototype result
`Synthetic Transfer Sweep 001` generated 864 deterministic synthetic runs; 853 are prospectively eligible after post-onset exclusions.

Grouped holdout prevents the same topology × seed-fraction × propagation-parameter configuration from appearing in both development and held-out source data.

- S0 static: full AUROC 0.829; unsafe-fraction baseline 0.884
- S1 dynamic rewiring: full AUROC 0.908; baseline 0.910
- S2 heterogeneous susceptibility: full AUROC 0.863; baseline 0.859

Because the source-regime full predictor does not have preregistered positive incremental AUROC over the simple baseline, transfer-retention ratios are reported as undefined.

## Scientific interpretation
The prototype validates the prospective-forecasting and cross-regime evaluation pipeline while demonstrating why high raw AUROC must not be confused with incremental predictive value over a cheap baseline.

## R1 verdict
`PASS — METHODOLOGY-HARDENED SCIENTIFIC PROTOTYPE`
