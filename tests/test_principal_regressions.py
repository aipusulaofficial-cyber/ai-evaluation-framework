import pytest

from evaluation_metrics import calibration_bins


@pytest.mark.parametrize("value", [float("nan"), float("inf"), -0.1, 1.1])
def test_invalid_confidence_rejected(value):
    with pytest.raises(ValueError):
        calibration_bins([value], [True])


def test_boundary_values_not_double_counted():
    bins = calibration_bins([0.0, 0.5, 1.0], [True, False, True], bins=2)
    assert sum(b["count"] for b in bins) == 3
