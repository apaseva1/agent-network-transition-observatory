# Agent Network Transition Observatory v1.0.0 — Release Notes

A reproducible synthetic research artifact for evaluating whether candidate population-level warning signals add predictive value beyond reactive baselines across dynamic network regimes.

## Status & Scientific Boundaries

**Scientific Status:** `PIPELINE_VALIDATED` / `SCIENTIFIC_HYPOTHESIS_NOT_ESTABLISHED`

- **No Canonical R1 Scientific Result Changed:** No underlying experimental code, data files, or metrics were modified for this v1.0.0 release.
- **Unfavorable Evidence Disclosed:** Current R1 does not establish positive incremental early-warning value.
  - **S0 (static):** Negative uplift
  - **S1 (rewire):** Approximately zero / slightly negative uplift
  - **S2 (heterogeneous):** Small positive uplift
  - **Transfer Retention:** Undefined under the current threshold rule.

## Reproduction Taxonomy

- **CANONICAL_ARTIFACT_INTEGRITY:** PASS
- **CROSS_PLATFORM_NUMERICAL_REPRODUCTION:** PASS
- **CANONICAL_EXACT_REPRODUCTION:** `NOT_VERIFIED_ON_THIS_PLATFORM` (canonical byte execution environment not fully reconstructed).

## Canonical Result Digests

- `results/synthetic_transfer_runs.csv`: `be3fa8e9e45b41420b7e31056fca7a6115c5c015e7ab6a53cd59d97d7ed39182`
- `results/synthetic_transfer_summary.json`: `b211e5854d5935050a9abdaea5e8c036f67e523cd08141b174fc82d07a03602a`

## Verification Instructions

```bash
python -m pytest -q
python scripts/verify_reproduction.py --integrity
python scripts/verify_reproduction.py --exact
python scripts/verify_reproduction.py --numerical
python scripts/run_v1_gate.py
```
