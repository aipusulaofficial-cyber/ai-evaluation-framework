import time
import uuid

from fastapi import FastAPI, HTTPException
from fastapi import Request as FastAPIRequest
from opentelemetry import trace
from pydantic import BaseModel, Field

from evaluation_domain import Case, exact_match
from observability import configure_observability, get_logger

configure_observability()
logger = get_logger(__name__)
tracer = trace.get_tracer("ai-evaluation-framework")
app = FastAPI(title="ai-evaluation-framework", version="1.0.0")


class EvaluationCasePayload(BaseModel):
    expected: str = Field(min_length=1, max_length=10_000)
    actual: str = Field(min_length=1, max_length=10_000)


class EvaluationPayload(BaseModel):
    cases: list[EvaluationCasePayload] = Field(min_length=1, max_length=10_000)


class Request(BaseModel):
    key: str = Field(min_length=1, max_length=128)
    payload: EvaluationPayload


@app.middleware("http")
async def observability_headers(request: FastAPIRequest, call_next):
    started = time.perf_counter()
    request_id = request.headers.get("x-request-id") or str(uuid.uuid4())
    correlation_id = request.headers.get("x-correlation-id") or request_id
    response = await call_next(request)
    response.headers["x-request-id"] = request_id
    response.headers["x-correlation-id"] = correlation_id
    response.headers["x-latency-ms"] = f"{(time.perf_counter() - started) * 1000:.3f}"
    return response


@app.get("/health/live")
def live() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/health/ready")
def ready() -> dict[str, str]:
    return {"status": "ready"}


@app.post("/v1/evaluate")
def handle(request: Request) -> dict[str, float | int]:
    with tracer.start_as_current_span("evaluation.evaluate") as span:
        span.set_attribute("evaluation.key", request.key)
        try:
            cases = [
                Case(id=str(index), expected=item.expected, actual=item.actual)
                for index, item in enumerate(request.payload.cases)
            ]
            scorecard = exact_match(cases)
            logger.info(
                "evaluation completed key=%s total=%s score=%s",
                request.key,
                scorecard.total,
                scorecard.score,
            )
            return {
                "total": scorecard.total,
                "passed": scorecard.passed,
                "score": scorecard.score,
            }
        except (ValueError, KeyError, TypeError) as exc:
            logger.warning("evaluation rejected key=%s reason=%s", request.key, exc)
            raise HTTPException(status_code=400, detail=str(exc)) from exc
