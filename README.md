# Agent Network Transition Observatory

Can population-level warning signals forecast future multi-agent cascades **better than simple reactive baselines**, and does that incremental advantage survive changes in topology, propagation parameters, dynamic rewiring, agent heterogeneity, model family, task, and experimental fidelity?

**Scientific Status**: `PIPELINE_VALIDATED` | `SCIENTIFIC_HYPOTHESIS_NOT_ESTABLISHED`

> [!WARNING]
> **Current Limitation & R1 Evidence Scale:**
> Current R1 finds no established positive incremental early-warning advantage: S0 negative uplift, S1 near zero, S2 small positive, transfer retention undefined.

> [!NOTE]
> **Proposed Higher-Fidelity Endpoint:**
> If funded under the submitted proposal, this repository will transition from deterministic synthetic simulations to frontier LLM cross-agent evaluations on Kubernetes.

## Current Artifact
- 864 deterministic synthetic transfer runs
- Canonical machine-readable results
- 3 graph families, 3 dynamics regimes
- 8 tests

## One-command Verification
```bash
python scripts/run_all.py
python scripts/run_v1_gate.py
```

## Documentation
- [Whitepaper](docs/WHITEPAPER.md)
- [Technical Review Packet](docs/GRANT_REVIEW_PACKET.md)
- [Results](docs/RESULTS.md)
- [Claim Boundary](CLAIM_BOUNDARY.md)
- [Reviewer Guide](docs/REVIEWER_GUIDE.md)
- [Documentation Index](docs/INDEX.md)
