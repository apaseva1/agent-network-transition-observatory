# Agent Network Transition Observatory — Technical Review Packet

## 1. Research Problem and Motivation
Multi-agent AI systems are complex dynamic networks. A local failure—such as a single agent entering a goal-misaligned loop—can propagate through delegation and message passing, eventually compromising the entire workflow. If intervention only occurs after a threshold of failure is explicitly reached, containment may be impossible.

The core research question we address is: **Can population-level warning signals forecast future multi-agent cascades better than simple reactive baselines, and does that incremental advantage survive changes in topology, propagation parameters, dynamic rewiring, agent heterogeneity, model family, task, and experimental fidelity?**

## 2. Current Architecture and Measurement Instrument
The Agent Network Transition Observatory (ANTO) currently serves as a highly controlled measurement instrument. To isolate the effects of dynamic network observables, we constructed a deterministic synthetic statistical pipeline rather than relying on noisy large language models. The R1 baseline executes 864 deterministic synthetic transfer runs representing different graph families and regimes.

The heart of the measurement is the **Transfer Retention Pipeline**. We evaluate the exact same underlying synthetic population across different features:
- **Full Predictor**: Uses current unsafe fraction, recent propagation rate, activity entropy, average clustering, algebraic connectivity, and edge-turnover fraction.
- **Baseline Predictor**: Uses only current unsafe fraction.

By evaluating the full predictor against the baseline, we calculate the marginal diagnostic contribution of the structural graph primitives in forecasting cascading failure.

## 3. Deterministic Reproducibility
The R1 baseline is built to be rigorously reproducible. Every aspect of the pipeline—from scenario generation to evaluation and metric calculation—is deterministic. 

Reviewers and collaborators can easily verify this exact scientific state locally by running:
```bash
python -m pytest -q
python scripts/verify_reproduction.py
python scripts/run_all.py
```
This produces machine-readable CSV and JSON metrics. A cryptographic SHA-256 digest of these canonical results is maintained in `results/reproduction_manifest.json`, ensuring that no unauthorized changes to the scientific evidence can slip past the verification gates.

## 4. Explicit Claim Boundary and Limitations
We maintain strict scientific discipline regarding what ANTO currently proves. **The R1 codebase implements a transfer retention pipeline, reproduces machine-readable results deterministically, measures forecasting contributions, and detects signal retention in synthetic scenarios.**

It does **not** prove the system safe, nor does it validate frontier-agent safety in production environments. 
The current R1 instrument is limited to a deterministic evaluator using hand-crafted synthetic runs, simplified topology assumptions, and boolean states. It does not evaluate missing traces, real agent behavior, semantic complexity, or the unstructured ambiguity inherent in real-world LLM-driven environments.

## 5. Funded Transition in Fidelity (The Roadmap)
The Schmidt Sciences 2026 grant enables us to transition this validated measurement pipeline to progressively higher-fidelity ecosystems:
1. **Stage 1 (Current R1)**: Deterministic evaluation of synthetic networks.
2. **Stage 2**: Scripted, tool-using agents replacing synthetic nodes.
3. **Stage 3**: Introduction of at least two independently developed open-weight model families acting as agents.
4. **Stage 4**: Integration of heterogeneous frontier APIs from multiple independent providers under a frozen configuration ledger, evaluating realistic dynamic rewiring.

Across all stages, the final public v1.0.0 gate explicitly enforces the boundary: `DETERMINISTIC_SYNTHETIC_R1 != FUNDED_HIGH_FIDELITY_ENDPOINT`.

## 6. Falsification Logic
The entire research program rests on falsifiable hypotheses. We will reject the hypothesis that a given network observable provides multi-agent safety value if:
- Added evidence fails to improve the targeted forecasting metric over the baseline.
- Any initial diagnostic improvements disappear when applied across heterogeneous model families or frontier APIs.
- The operational overhead of calculating the observable completely outweighs the benefits of early intervention.
