# v0.1.0-rfp — Research Prototype Candidate

Frozen for grant-feasibility evidence.

Includes:

- deterministic seeded network simulator;
- ER, Watts–Strogatz, and Barabási–Albert topologies;
- static, dynamically rewired, and heterogeneous synthetic regimes;
- prospective forecast eligibility rule;
- candidate population observables;
- simple unsafe-fraction baseline;
- full-observable logistic predictor;
- cross-regime transfer-retention calculation;
- unit tests and machine-readable results;
- explicit falsification and claim boundaries.

No LLM or frontier-agent result is claimed in this release.


# Methodological Hardening R2

The source-regime split is now grouped by topology × seed fraction × propagation parameter, preventing replicate configurations from leaking across development and held-out sets.

Verification: **8 passed**.

This change was made before submission freeze because it reduces the chance that the prototype overstates evidence quality. All generated CSV/JSON outputs in this capsule were regenerated after the change.
