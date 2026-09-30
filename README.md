# AI Evaluation Framework

[![CI](https://github.com/aipusulaofficial-cyber/ai-evaluation-framework/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/aipusulaofficial-cyber/ai-evaluation-framework/actions/workflows/ci.yml)
[![Production Tests](https://github.com/aipusulaofficial-cyber/ai-evaluation-framework/actions/workflows/production-tests.yml/badge.svg?branch=main)](https://github.com/aipusulaofficial-cyber/ai-evaluation-framework/actions/workflows/production-tests.yml)
[![Security / SBOM](https://github.com/aipusulaofficial-cyber/ai-evaluation-framework/actions/workflows/security-sbom.yml/badge.svg?branch=main)](https://github.com/aipusulaofficial-cyber/ai-evaluation-framework/actions/workflows/security-sbom.yml)


A repeatable evaluation framework for measuring AI system behavior with versioned protocols, calibration, adjudication, agreement measurement and audit-ready evidence.

## Evaluation lifecycle
```text
Dataset + rubric version
        -> evaluator / judge
        -> independent scoring
        -> calibration
        -> adjudication
        -> agreement measurement
        -> evaluation evidence
```

The design goal is reproducibility: every result is tied to the dataset, rubric, evaluator configuration and run metadata that produced it.

## Core contracts
- Dataset and rubric versions are explicit.
- Judge/model adapters are replaceable.
- Scoring rules are deterministic where the evaluator permits it.
- Disagreements can be adjudicated instead of silently collapsed.
- Agreement is measured separately from the final score.
- Run metadata provides an audit trail.

## Reliability
Malformed datasets, invalid rubrics, evaluator failures and ambiguous outcomes are explicit states. External model dependencies are isolated behind adapters so tests remain deterministic.

## Quality gates
Contract, edge-case and failure-path tests run in CI alongside security and production validation.

## Evidence
- Engineering contract: [docs/PRINCIPAL-ENGINEERING.md](docs/PRINCIPAL-ENGINEERING.md)
- Architecture: [ARCHITECTURE.md](ARCHITECTURE.md)
- Decisions: [ADRs](ADRs/)

This is an implementation-oriented evaluation system, not a collection of benchmark prompts.

## Portfolio evidence
[Portfolio evidence map](docs/PORTFOLIO_EVIDENCE.md) — executable proof, architecture mapping and reviewable CI evidence.
