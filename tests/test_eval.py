import pytest

from ai_eval import Case, RegressionGate, exact_match


def test_exact_match():
    assert exact_match([Case("1", "A", "a"), Case("2", "B", "C")]) == 0.5


def test_gate():
    RegressionGate(0.8).check(0.8)


def test_gate_blocks_regression():
    with pytest.raises(AssertionError):
        RegressionGate(0.8).check(0.79)


def test_empty_dataset():
    assert exact_match([]) == 0
