"""Deterministic AI evaluation framework with regression gates."""

from dataclasses import dataclass
from statistics import mean


@dataclass(frozen=True)
class Case:
    id: str
    expected: str
    actual: str


def exact_match(cases):
    return (
        mean(c.expected.strip().lower() == c.actual.strip().lower() for c in cases)
        if cases
        else 0.0
    )


class RegressionGate:
    def __init__(self, minimum):
        self.minimum = minimum

    def check(self, score):
        if score < self.minimum:
            raise AssertionError(f"score {score:.3f} below gate {self.minimum:.3f}")
        return True
