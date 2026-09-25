from dataclasses import dataclass


@dataclass(frozen=True)
class Case:
    id: str
    expected: str
    actual: str


@dataclass(frozen=True)
class Scorecard:
    total: int
    passed: int
    score: float


def exact_match(cases: list[Case], threshold: float = 0.9) -> Scorecard:
    if not cases:
        raise ValueError("empty dataset")
    if not 0 <= threshold <= 1:
        raise ValueError("invalid threshold")
    passed = sum(c.expected.strip() == c.actual.strip() for c in cases)
    score = passed / len(cases)
    return Scorecard(len(cases), passed, score)


def regression_gate(scorecard: Scorecard, threshold: float) -> bool:
    return scorecard.score >= threshold
