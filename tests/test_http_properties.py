from fastapi.testclient import TestClient
from hypothesis import given, strategies as st

from service import app

client = TestClient(app)


def test_contract() -> None:
    assert client.get("/health/live").status_code == 200


@given(st.text(alphabet=st.characters(blacklist_categories=("Cs",)), min_size=1, max_size=32).filter(lambda value: value.strip()))
def test_property(value: str) -> None:
    response = client.post(
        "/v1/evaluate",
        json={
            "key": value,
            "payload": {"cases": [{"expected": value, "actual": value}]},
        },
    )
    assert response.status_code == 200, response.text
