from typing import Iterable


def source_recall(expected: Iterable[str], retrieved: Iterable[str]) -> float:
    """
    Recall = retrieved relevant / expected relevant
    """

    expected = set(expected)
    retrieved = set(retrieved)

    if not expected:
        return 0.0

    return len(expected & retrieved) / len(expected)


def source_precision(expected: Iterable[str], retrieved: Iterable[str]) -> float:
    """
    Precision = retrieved relevant / total retrieved
    """

    expected = set(expected)
    retrieved = set(retrieved)

    if not retrieved:
        return 0.0

    return len(expected & retrieved) / len(retrieved)


def source_f1(expected: Iterable[str], retrieved: Iterable[str]) -> float:

    precision = source_precision(expected, retrieved)
    recall = source_recall(expected, retrieved)

    if precision + recall == 0:
        return 0.0

    return 2 * precision * recall / (precision + recall)


def exact_match(expected: str, generated: str) -> bool:

    return expected.strip().lower() == generated.strip().lower()

def answer_overlap(expected: str, generated: str) -> float:
    """
    Measures the fraction of unique words in the expected answer
    that also appear in the generated answer.
    """

    expected_words = set(expected.lower().split())
    generated_words = set(generated.lower().split())

    if not expected_words:
        return 0.0

    return len(expected_words & generated_words) / len(expected_words)