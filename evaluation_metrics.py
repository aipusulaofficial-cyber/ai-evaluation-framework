def exact_match(predictions: list[str], references: list[str]) -> float:
    if len(predictions) != len(references) or not predictions:
        raise ValueError("aligned non-empty datasets required")
    return sum(a.strip() == b.strip() for a, b in zip(predictions, references)) / len(predictions)


def calibration_bins(
    confidences: list[float], outcomes: list[bool], bins: int = 10
) -> list[dict]:
    if len(confidences) != len(outcomes) or not confidences:
        raise ValueError("aligned data required")
    if isinstance(bins, bool) or not isinstance(bins, int) or bins < 1:
        raise ValueError("bins must be a positive integer")
    if any(not 0 <= confidence <= 1 for confidence in confidences):
        raise ValueError("confidences must be finite and in [0, 1]")

    result = []
    for index in range(bins):
        lower, upper = index / bins, (index + 1) / bins
        # Include exactly 1.0 in the final bin, never in an adjacent bin.
        pairs = [
            (confidence, outcome)
            for confidence, outcome in zip(confidences, outcomes)
            if lower <= confidence < upper
            or (index == bins - 1 and confidence == 1.0)
        ]
        if pairs:
            result.append(
                {
                    "lower": lower,
                    "upper": upper,
                    "count": len(pairs),
                    "confidence": sum(confidence for confidence, _ in pairs) / len(pairs),
                    "accuracy": sum(outcome for _, outcome in pairs) / len(pairs),
                }
            )
    return result


def label_agreement(a: list[str], b: list[str]) -> float:
    if len(a) != len(b) or not a:
        raise ValueError("aligned non-empty labels required")
    return sum(x == y for x, y in zip(a, b)) / len(a)
