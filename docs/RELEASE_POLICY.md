# Release Policy

## Versioning

Repository releases follow semantic versioning for the research artifact:

- **PATCH** — documentation, packaging, or non-semantic bug fixes that do not alter canonical outputs.
- **MINOR** — new experiments, metrics, tests, or methodological hardening that preserves the overall research question.
- **MAJOR** — incompatible changes to the research object, primary evaluation contract, or evidence semantics.

## Evidence rule

Every release that changes canonical machine-readable results must include:

1. regenerated outputs;
2. updated `results/reproduction_manifest.json`;
3. passing unit tests;
4. passing `scripts/verify_reproduction.py`;
5. an explicit changelog entry;
6. an updated claim boundary if scientific interpretation changes.

## Frozen submission

The Schmidt Sciences v14 submission freeze is external historical provenance, not a moving release target.
