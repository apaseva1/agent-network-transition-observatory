# Contributing

This is a research repository, so code changes and scientific claims are reviewed separately.

## Required before merging

1. `python -m pytest -q` passes.
2. `python scripts/verify_reproduction.py` passes when the committed result contract is intended to remain unchanged.
3. Any intended result change includes regenerated machine-readable outputs and a changelog entry.
4. New scientific claims state their evaluation regime and do not silently generalize beyond the evidence.
5. Changes after the Schmidt v14 submission freeze are labeled as post-freeze repository work.

## Result-changing pull requests

A pull request that intentionally changes canonical outputs should explain:

- what changed in the method;
- why the old result is superseded;
- which tests protect the new invariant;
- whether the claim boundary changes;
- the new reproduction-manifest digest.

Do not edit result files manually.
