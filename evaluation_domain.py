from dataclasses import dataclass
from statistics import mean

@dataclass(frozen=True)
class Case: id:str; expected:str; actual:str
@dataclass(frozen=True)
class Scorecard: total:int; passed:int; score:float

def exact_match(cases:list[Case],threshold:float=.9)->Scorecard:
    if not cases: raise ValueError("empty dataset")
    passed=sum(c.expected.strip()==c.actual.strip() for c in cases); score=passed/len(cases)
    if not 0<=threshold<=1: raise ValueError("invalid threshold")
    return Scorecard(len(cases),passed,score)

def regression_gate(scorecard:Scorecard,threshold:float)->bool:
    return scorecard.score>=threshold
