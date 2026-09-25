from dataclasses import dataclass


@dataclass(frozen=True)
class Case:
    id: str
    expected: str
    actual: str

    def __post_init__(self) -> None:
        if not self.id.strip():
            raise ValueError("case id is required")


@dataclass(frozen=True)
class Scorecard:
    total: int
    passed: int
    score: float

    def __post_init__(self) -> None:
        if self.total < 0 or self.passed < 0 or self.passed > self.total:
            raise ValueError("invalid scorecard counts")
        if not 0 <= self.score <= 1:
            raise ValueError("score must be between 0 and 1")


def exact_match(cases: list[Case], threshold: float = 0.9) -> Scorecard:
    if not cases:
        raise ValueError("empty dataset")
    if not 0 <= threshold <= 1:
        raise ValueError("invalid threshold")
    passed = sum(case.expected.strip() == case.actual.strip() for case in cases)
    score = passed / len(cases)
    return Scorecard(total=len(cases), passed=passed, score=score)


def regression_gate(scorecard: Scorecard, threshold: float) -> bool:
    if not 0 <= threshold <= 1:
        raise ValueError("invalid threshold")
    return scorecard.score >= threshold
