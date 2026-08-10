# Reviewer Guide: ANTO V1

This guide accompanies the Agent Network Transition Observatory (ANTO) `v1.0.0-rc.1` repository freeze for the Schmidt Sciences 2026 grant proposal.

## 1. Context for Reviewers
The submitted proposal ("Cross-Fidelity Early Warning of Cascading Failure in Dynamic AI Agent Networks") describes a multi-stage methodology for evaluating structural network observables as early-warning indicators for multi-agent cascades.

This repository implements **Stage 1 (R1)** of that methodology. It is a deterministic, synthetic measurement instrument designed to test the statistical transfer-analysis pipeline.

## 2. What to Evaluate
Reviewers should evaluate the repository as a **methodological proof-of-concept**, specifically verifying:
- The clarity and rigor of the `synthetic_transfer_sweep.py` experimental protocol.
- The statistical soundness of the transfer-retention pipeline, which isolates structural predictive advantage over a reactive baseline.
- The engineering discipline ensuring exact reproducibility of the canonical results.

## 3. What NOT to Evaluate
Reviewers should **not** evaluate this repository as:
- A proof that these observables predict real LLM-agent behavior.
- A functional safety tool for production deployment.

## 4. The Funded High-Fidelity Endpoint
As per the core grant philosophy, the synthetic R1 pipeline serves as the strict, deterministic baseline. The funded trajectory transitions this identical methodology to evaluate actual frontier API agents, verifying if the `DETERMINISTIC/SYNTHETIC R1` findings truly hold as the `FUNDED HIGH-FIDELITY ENDPOINT`.

## 5. Verification Instructions
To independently verify the synthetic claims:
```bash
# Clone the repository
git clone <url>
cd agent-network-transition-observatory

# Run the complete reproducibility suite
python scripts/run_all.py
```
This ensures the environment yields the exact same canonical `synthetic_transfer_summary.json` matrix submitted in the proposal.
