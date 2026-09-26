from fastapi.testclient import TestClient
from hypothesis import given
from hypothesis import strategies as st

from service import app

client = TestClient(app)


def test_contract() -> None:
    assert client.get("/health/live").status_code == 200


@given(st.text(min_size=1, max_size=32).filter(lambda value: value.strip()))
def test_property(value: str) -> None:
    response = client.post(
        "/v1/evaluate",
        json={
            "key": value,
            "payload": {"cases": [{"expected": value, "actual": value}]},
        },
    )
    assert response.status_code == 200, response.text


def test_rejects_empty_cases() -> None:
    response = client.post(
        "/v1/evaluate",
        json={"key": "run-1", "payload": {"cases": []}},
    )
    assert response.status_code == 422


def test_rejects_oversized_case_batch() -> None:
    cases = [{"expected": "x", "actual": "x"}] * 10_001
    response = client.post(
        "/v1/evaluate",
        json={"key": "run-1", "payload": {"cases": cases}},
    )
    assert response.status_code == 422
