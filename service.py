from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from opentelemetry import trace
from evaluation_domain import *
try:
 from opentelemetry.sdk.resources import Resource
 from opentelemetry.sdk.trace import TracerProvider
 from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
 p=TracerProvider(resource=Resource.create({"service.name":"ai-evaluation-framework"}));p.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()));trace.set_tracer_provider(p)
except Exception: pass
app=FastAPI(title="ai-evaluation-framework",version="1.0.0");tracer=trace.get_tracer("ai-evaluation-framework")
class Request(BaseModel): key:str; payload:dict={}
@app.get("/health/live")
def live(): return {"status":"ok"}
@app.get("/health/ready")
def ready(): return {"status":"ready"}
@app.post("/v1/evaluate")
def handle(r:Request):
 with tracer.start_as_current_span("ai-evaluation-framework.domain"):
  try: cases=[Case(str(i),str(x.get("expected","")),str(x.get("actual",""))) for i,x in enumerate(r.payload.get("cases",[]))];s=exact_match(cases);return {"total":s.total,"passed":s.passed,"score":s.score}
  except (ValueError,KeyError,RuntimeError) as e: raise HTTPException(status_code=400,detail=str(e)) from e
