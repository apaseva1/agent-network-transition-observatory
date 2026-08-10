# Agent Network Transition Observatory

Research prototype for testing whether population-level early-warning signals retain incremental predictive value for cascading failure as AI-agent systems increase in ecological fidelity.

## Status

`v0.3.0 POST-FREEZE REPOSITORY-HARDENED RESEARCH PROTOTYPE`

Companion to the frozen Schmidt Sciences 2026 proposal:

**Cross-Fidelity Early Warning of Cascading Failure in Dynamic AI Agent Networks**

The proposal is frozen separately. Repository evolution does not retroactively modify the submitted science.

## Research question

Can population-level warning signals forecast future multi-agent cascades **better than simple reactive baselines**, and does that incremental advantage survive changes in topology, propagation parameters, dynamic rewiring, agent heterogeneity, model family, task, and experimental fidelity?

## R1 synthetic observatory

The deterministic sweep crosses:
- 3 graph families
- 3 dynamics regimes
- 3 initial seed fractions
- 4 propagation parameters
- 8 deterministic replicates

Total: **864 runs**.

## Leakage-resistant holdout

The hardened source split is grouped by:

`topology × seed_fraction × propagation_parameter`

so replicates from the same synthetic configuration cannot appear in both development and held-out data.

## Predictor and baseline

Full predictor:
- unsafe fraction
- propagation rate
- activity entropy
- average clustering
- algebraic connectivity
- edge turnover

Baseline:
- current unsafe fraction only

Transfer retention is reported only when source uplift over the same baseline rule is sufficiently positive.

## Reproduce

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m experiments.synthetic_transfer_sweep
```

Expected current verification:

```text
8 passed
STATUS: PIPELINE_VALIDATED
SCIENTIFIC_HYPOTHESIS: NOT_ESTABLISHED
```

## Claim boundary

The R1 simulator validates the forecasting and transfer-evaluation pipeline. It does **not** establish that synthetic graph observables predict cascades in LLM-agent populations.

## Licensing

No open-source license is granted yet. All rights are reserved pending an explicit licensing decision.

## Repository quality gates

```bash
python scripts/run_all.py
```

This runs the unit-test suite and then regenerates the canonical synthetic outputs and checks them against normalized cross-platform digests in `results/reproduction_manifest.json`.

See `docs/ARCHITECTURE.md`, `docs/RELEASE_POLICY.md`, and `docs/PUBLICATION_CHECKLIST.md`.
