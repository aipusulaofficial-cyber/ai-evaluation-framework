from collections import Counter
from math import comb


def exact_match(predictions: list[str], references: list[str]) -> float:
    if len(predictions) != len(references) or not predictions: raise ValueError("aligned non-empty datasets required")
    return sum(a.strip() == b.strip() for a,b in zip(predictions,references)) / len(predictions)


def calibration_bins(confidences: list[float], outcomes: list[bool], bins: int = 10) -> list[dict]:
    if len(confidences) != len(outcomes) or not confidences: raise ValueError("aligned data required")
    if bins < 1: raise ValueError("bins must be positive")
    result=[]
    for i in range(bins):
        lo=i/bins; hi=(i+1)/bins
        pairs=[(c,o) for c,o in zip(confidences,outcomes) if lo <= c <= hi if i == bins-1 else lo <= c < hi]
        if pairs: result.append({"lower":lo,"upper":hi,"count":len(pairs),"confidence":sum(c for c,_ in pairs)/len(pairs),"accuracy":sum(o for _,o in pairs)/len(pairs)})
    return result


def label_agreement(a: list[str], b: list[str]) -> float:
    if len(a) != len(b) or not a: raise ValueError("aligned non-empty labels required")
    return sum(x==y for x,y in zip(a,b))/len(a)
