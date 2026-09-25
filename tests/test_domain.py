import pytest

from evaluation_domain import Case, Scorecard, exact_match, regression_gate


def test_eval_gate() -> None:
    scorecard = exact_match([Case("1", "a", "a"), Case("2", "b", "x")])
    assert scorecard.passed == 1
    assert not regression_gate(scorecard, 0.9)


def test_empty_dataset_rejected() -> None:
    with pytest.raises(ValueError, match="empty dataset"):
        exact_match([])


def test_invalid_threshold_rejected() -> None:
    with pytest.raises(ValueError, match="invalid threshold"):
        regression_gate(Scorecard(1, 1, 1.0), 1.1)


def test_scorecard_invariants() -> None:
    with pytest.raises(ValueError, match="invalid scorecard counts"):
        Scorecard(1, 2, 1.0)
