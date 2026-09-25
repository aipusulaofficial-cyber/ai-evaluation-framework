# ADR-0002: Production hardening
FastAPI is the edge contract; OpenTelemetry is the telemetry boundary; Kubernetes and Helm define runtime packaging; Terraform owns infrastructure inputs. Trivy and CycloneDX gate security/SBOM; contract and Hypothesis tests protect evaluation APIs; Locust provides load scenarios.
Failure handling stays explicit through health probes and bounded resources. Production externalizes datasets, state, secrets and telemetry.
