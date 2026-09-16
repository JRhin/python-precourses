import pytest

from src.boolean_operators import (
    both_true,
    either_true,
    exactly_one,
    implies,
    is_in_range,
    majority_vote,
)


@pytest.mark.parametrize(
    "x, low, high, expected",
    [
        (5, 0, 10, True),
        (-1, 0, 10, False),
        (0, 0, 10, True),
        (10, 0, 10, True),
        (5.5, 0, 10, True),
        (11, 0, 10, False),
        (-0.1, 0, 10, False),
        (3, 3, 3, True),
        (2, 3, 5, False),
        (4, 3, 5, True),
    ],
)
def test_is_in_range(x, low, high, expected):
    assert is_in_range(x, low, high) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [(True, True, True), (True, False, False), (False, True, False), (False, False, False)] * 3,
)
def test_both_true(a, b, expected):
    assert both_true(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [(False, True, True), (False, False, False), (True, False, True), (True, True, True)] * 3,
)
def test_either_true(a, b, expected):
    assert either_true(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [(True, False, True), (True, True, False), (False, False, False), (False, True, True)] * 3,
)
def test_exactly_one(a, b, expected):
    assert exactly_one(a, b) == expected


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (True, True, True, True),
        (True, True, False, True),
        (True, False, False, False),
        (False, False, False, False),
        (False, True, True, True),
        (True, False, True, True),
        (False, False, True, False),
        (False, True, False, False),
        (True, True, True, True),
        (False, False, False, False),
    ],
)
def test_majority_vote(a, b, c, expected):
    assert majority_vote(a, b, c) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [(True, True, True), (True, False, False), (False, True, True), (False, False, True)] * 3,
)
def test_implies(a, b, expected):
    assert implies(a, b) == expected
