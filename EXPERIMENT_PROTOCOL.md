# Experiment Protocol — Synthetic Transfer Sweep 001

## Purpose

Validate the dynamic-network measurement and transfer-analysis pipeline before using any language-model agents.

## Network topologies

- Erdős–Rényi
- Watts–Strogatz small-world
- Barabási–Albert scale-free

## Synthetic regimes

- `S0_static`: fixed topology, homogeneous propagation susceptibility;
- `S1_rewire`: dynamic edge rewiring during propagation;
- `S2_heterogeneous`: fixed topology with node-level susceptibility heterogeneity.

These are **not** presented as real agent-fidelity levels.

## Candidate observables at forecast time

- current unsafe fraction;
- recent propagation rate;
- activity entropy;
- average clustering;
- algebraic connectivity (second-smallest Laplacian eigenvalue);
- edge-turnover fraction.

## Prediction target

Only runs that have **not** crossed the 0.50 cascade threshold by the observation time are eligible for forecasting. An eligible run is labeled `future_cascade=1` if it crosses the threshold later in the forecast horizon.

## Evaluation

A logistic-regression predictor using the full candidate-observable vector is trained on eligible `S0_static` runs and evaluated on held-out `S0_static`, `S1_rewire`, and `S2_heterogeneous` runs. A second predictor using only current unsafe fraction is the simple baseline. Transfer retention measures the transferred **advantage over this baseline**, not raw AUROC above chance.

Reported metrics:

- AUROC;
- average precision (AUPRC);
- Brier score;
- cascade prevalence;
- transfer retention of predictive advantage over the same current-unsafe-fraction baseline, when source-regime uplift is sufficiently positive.

## Claim boundary

This experiment validates the statistical pipeline only. It does not show transfer to LLM or frontier-agent populations.

## Transfer reporting guard

The analysis reports absolute predictive uplift over the simple baseline at every target regime. A transfer-retention ratio is reported only when source-regime uplift is at least 0.01 AUROC in the prototype; weaker source uplift is treated as insufficient for a stable ratio. The funded study will preregister the corresponding threshold and primary scoring rule before higher-fidelity experiments.
