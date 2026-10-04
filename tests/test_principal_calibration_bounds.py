import pytest

from evaluation_metrics import calibration_bins


def test_boundary_confidence_is_counted_once():
    result = calibration_bins([0.0, 0.5, 1.0], [False, True, True], bins=2)
    assert sum(row["count"] for row in result) == 3
    assert [row["count"] for row in result] == [1, 2]


@pytest.mark.parametrize("bins", [0, -1, 1.5, True, "10"])
def test_invalid_bin_count_is_rejected(bins):
    with pytest.raises(ValueError, match="positive integer"):
        calibration_bins([0.5], [True], bins=bins)


@pytest.mark.parametrize("confidence", [float("nan"), float("inf"), -0.1, 1.1, "0.5", True])
def test_invalid_confidence_is_rejected(confidence):
    with pytest.raises(ValueError):
        calibration_bins([confidence], [True])
