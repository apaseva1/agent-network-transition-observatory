# Canonical Execution Envelope

This document defines the strict reproduction semantics and verification boundaries for the Agent Network Transition Observatory (ANTO) R1 synthetic transfer sweep.

Due to the fundamental nature of cross-platform floating-point arithmetic and varying underlying linear algebra backends (BLAS/LAPACK), exact bit-for-bit reproduction of network science observables (such as algebraic connectivity via eigenvalue decomposition) across different operating systems or hardware architectures is not guaranteed. 

To preserve epistemic rigor without inducing false-positive reproduction failures, we formally distinguish three levels of scientific reproduction:

## A. CANONICAL_ARTIFACT_INTEGRITY
**Definition:** Exact cryptographic identity of the committed scientific artifacts.
**Mechanism:** The `verify_reproduction.py --integrity` gate asserts that the SHA-256 digests of the canonical output files (`synthetic_transfer_runs.csv` and `synthetic_transfer_summary.json`) exactly match the immutable hashes stored in `results/reproduction_manifest.json`.

## B. CANONICAL_EXACT_REPRODUCTION
**Definition:** Fresh recomputation that reproduces the canonical normalized artifacts exactly, down to the byte level, with zero floating-point drift.
**Status on Current Platforms:** Often `NOT_VERIFIED_ON_THIS_PLATFORM` on ordinary developer or CI machines running Windows, macOS, or differing Linux environments.
**Mechanism:** The `verify_reproduction.py --exact` gate performs a fresh isolated execution of the scientific pipeline and asserts exact cryptographic equivalence of the regenerated artifacts against the canonical manifest.

## C. CROSS_PLATFORM_NUMERICAL_REPRODUCTION
**Definition:** Fresh recomputation with exact structural, categorical, and integer identity, bounded by an explicit floating-point tolerance for continuous algebraic observables.
**Mechanism:** The `verify_reproduction.py --numerical` gate asserts that all row structures, string identities, integer identifiers, and keys are mathematically identical to the canonical artifacts, while explicitly tolerating a relative float drift of up to `1e-9` (empirically observed maximum drift is `~5e-14` across standard platforms). 

## Canonical Byte Execution Environment
**Status:** `NOT_FULLY_RECONSTRUCTED`

The specific combination of OS kernel, glibc, NumPy build flags, and specific BLAS backend (e.g. OpenBLAS vs MKL) that produced the original R1 frozen submission artifacts has not been universally reconstructed for all possible test environments. Therefore, achieving `NOT_VERIFIED_ON_THIS_PLATFORM` on the exact gate while passing the numerical gate constitutes a valid, non-falsifying reproduction of the scientific pipeline.
