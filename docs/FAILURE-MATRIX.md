# Failure matrix

| Failure | Detection | Action | Retry? | Impact |
|---|---|---|---|---|
| Invalid input | validation | reject | No | 4xx |
| Dependency timeout | timeout budget | normalize | Safe/idempotent only | bounded failure/degradation |
| Dependency error | adapter | exponential backoff | Safe/idempotent only | bounded latency |
| Repeated failure | circuit breaker | open circuit | No while open | fast failure |
| Overload | bounded executor/rate limiter | fail fast/degrade | No | 429/degraded |
| Telemetry failure | exporter error | preserve domain result | exporter-local | no domain corruption |

Dataset/evaluator failure -> explicit failed evaluation; evaluator timeout -> bounded retry only for deterministic/idempotent evaluation; regression gate must fail closed; partial scorecards are marked incomplete.