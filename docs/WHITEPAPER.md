# Agent Network Transition Observatory:
## Cross-Fidelity Early Warning of Cascading Failure in Dynamic AI Agent Networks

**Author:** Anna Paseva
**Role:** Independent Researcher; Principal Network Analyst
**Repository whitepaper version:** 1.0-draft
**Date:** 2026-08

## Abstract

As AI agents interact in increasingly dense networks, cascading failures—where one compromised or hallucinating agent triggers a chain reaction of failures—become a systemic risk. The central safety question is whether we can detect early-warning signals at the population level *before* the cascade becomes irrecoverable, and whether those signals transfer robustly across changes in network topology and agent capability. This whitepaper introduces the Agent Network Transition Observatory (ANTO), a deterministic research prototype designed to validate a pipeline for forecasting cascading failures using structural graph observables.

The current R1 instrument evaluates 864 deterministic synthetic transfer runs across three graph families and three synthetic regimes (static, rewiring, heterogeneous). A key finding is that the transfer retention pipeline successfully isolates the incremental predictive value of population-level observables (like activity entropy and edge turnover) over a simple reactive baseline (current unsafe fraction). However, the current scientific boundary is strictly methodological: the results are deterministic synthetic metrics, not evidence that these signals predict cascades in real LLM-agent deployments. This paper outlines the higher-fidelity research question and the falsifiable roadmap toward real open-weight and frontier-agent populations.

## 1. Introduction

Multi-agent AI systems are complex dynamic networks. A local failure—such as a single agent entering a goal-misaligned loop—can propagate through delegation and message passing, eventually compromising the entire workflow. If intervention only occurs after a threshold of failure is explicitly reached, containment may be impossible.

This prototype investigates whether we can extract population-level warning signals (e.g., changes in algebraic connectivity, clustering, or activity entropy) that forecast a cascade *before* it occurs. Crucially, any forecasting advantage must be evaluated against a simple reactive baseline (e.g., reacting purely to the current number of unsafe agents) and must survive transfer to unseen network dynamics.

We do not claim that the current synthetic evidence automatically applies to real LLM populations. Instead, this instrument validates the statistical transfer-analysis pipeline under controlled conditions.

## 2. Research Question

The primary falsifiable question is:
**Can population-level warning signals forecast future multi-agent cascades better than simple reactive baselines, and does that incremental advantage survive changes in topology, propagation parameters, dynamic rewiring, agent heterogeneity, model family, task, and experimental fidelity?**

The current R1 sub-question is whether a deterministic statistical pipeline can successfully measure this transfer retention. The funded higher-fidelity hypothesis asks whether these benefits hold in real LLM-driven environments with semantic ambiguity and partial observability.

## 3. Formal System Model

### Definitions
- **node**: An executing agent in the network.
- **edge**: An active communication or delegation channel.
- **unsafe fraction**: The proportion of compromised nodes at observation time.
- **propagation parameter**: The probability of failure spreading across an edge.
- **cascade threshold**: The threshold (0.50 fraction of nodes compromised) defining a systemic failure.
- **forecast horizon**: The future time window over which a cascade is predicted.

### Model Assumptions
This formal model is a conceptual abstraction. The current R1 codebase implements a deterministic, simplified synthetic simulation of these constructs.

## 4. Evaluator Semantics

The R1 deterministic evaluator extracts specific observables at observation time from runs that have *not* yet crossed the cascade threshold.

- **Full Predictor**: Uses current unsafe fraction, recent propagation rate, activity entropy, average clustering, algebraic connectivity, and edge-turnover fraction.
- **Baseline Predictor**: Uses only current unsafe fraction.

Transfer retention measures the transferred **advantage over this baseline**, not raw AUROC above chance, ensuring that the structural signals add genuine predictive value.

## 5. R1 Experimental Design

The current R1 experiment executes **864 deterministic synthetic transfer runs**. The deterministic sweep crosses:
- 3 graph families (Erdős–Rényi, Watts–Strogatz, Barabási–Albert)
- 3 dynamics regimes (S0_static, S1_rewire, S2_heterogeneous)
- 3 initial seed fractions
- 4 propagation parameters
- 8 deterministic replicates

A logistic-regression predictor is trained on eligible `S0_static` runs and evaluated on held-out `S0_static`, `S1_rewire`, and `S2_heterogeneous` runs.

## 6. Interpretation

The R1 prototype establishes:
- An operational synthetic pipeline for evaluating population-level early-warning signals.
- A statistically robust transfer-retention metric that penalizes simple reactive advantages.
- Deterministic reproducibility of the synthetic surface.

R1 does **not** establish:
- Real-world safety forecasting in frontier-agent deployments.
- The existence of these specific structural signals in open-ended LLM networks.

## 7. Limitations

Reviewers must explicitly acknowledge the following bounds of the R1 instrument:
- Evaluates purely synthetic, deterministic networks.
- All regimes are synthetic instrumentation regimes; none are LLM/frontier-agent fidelity levels.
- Assumes absence of LLM agents, heterogeneous model families, and frontier APIs.
- External validity is not established.

## 8. Higher-Fidelity Research Program

The Schmidt Sciences 2026 grant enables a staged progression toward ecological fidelity:
- **Stage 2**: Scripted/tool-using agents in static networks.
- **Stage 3**: At least two independently developed open-weight model families.
- **Stage 4**: Heterogeneous frontier API populations from at least two independent providers, examining realistic dynamic rewiring.

Across all stages, we explicitly verify the DETERMINISTIC/SYNTHETIC R1 = FUNDED HIGH-FIDELITY ENDPOINT mandate.

## 9. Conclusion

ANTO currently provides a reproducible measurement instrument and statistical transfer pipeline, not a proven safety mechanism. It formalizes a methodology for measuring the predictive value of dynamic structural observables, creating a falsifiable foundation for future frontier-agent evaluation.
