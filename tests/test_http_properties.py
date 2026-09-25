from hypothesis import given,strategies as st
from fastapi.testclient import TestClient
from service import app
c=TestClient(app)
def test_contract(): assert c.get("/health/live").status_code==200
@given(st.text(min_size=1,max_size=32))
def test_property(v):
 assert c.post("/v1/evaluate",json={"key":v,"payload":{"cases":[{"expected":v,"actual":v}]}}).status_code==200
