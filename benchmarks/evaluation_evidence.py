import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import json
from evaluation_domain import Case,exact_match,regression_gate
r=exact_match([Case("1","yes","yes"),Case("2","yes","no"),Case("3","no","no")]); report={"total":r.total,"passed":r.passed,"score":r.score,"gate_0_66":regression_gate(r,0.66),"gate_0_67":regression_gate(r,0.67)}
if report["score"]!=2/3 or not report["gate_0_66"] or report["gate_0_67"]: raise SystemExit(report)
print(json.dumps(report, sort_keys=True))
