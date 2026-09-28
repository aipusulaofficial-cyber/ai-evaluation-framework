from evaluation_domain import Case, exact_match, regression_gate


def test_exact_match_scorecard_and_regression_gate():
    scorecard = exact_match([Case("1", "yes", "yes"), Case("2", "no", "yes")])
    assert scorecard.total == 2
    assert scorecard.passed == 1
    assert scorecard.score == 0.5
    assert regression_gate(scorecard, 0.5) is True
    assert regression_gate(scorecard, 0.9) is False
