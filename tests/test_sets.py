import pytest

from src.sets import (
    common_elements,
    is_disjoint,
    is_subset,
    only_in_first,
    symmetric_difference_manual,
    unique_elements,
)


@pytest.mark.parametrize(
    "items, expected",
    [
        ([1, 2, 2, 3], {1, 2, 3}),
        ([], set()),
        ([1, 1, 1], {1}),
        (["a", "b", "a"], {"a", "b"}),
        ([1, 2, 3], {1, 2, 3}),
        ([True, 1], {True}),
        ([0, 0], {0}),
        ([5], {5}),
        ([1, 2, 3, 2, 1], {1, 2, 3}),
        (["x", "y", "x"], {"y", "x"}),
    ],
)
def test_unique_elements(items, expected):
    assert unique_elements(items) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([1, 2, 3], [2, 3, 4], {2, 3}),
        ([1, 2], [3, 4], set()),
        ([], [1], set()),
        ([1, 2, 3], [1, 2, 3], {1, 2, 3}),
        (["a", "b"], ["b", "c"], {"b"}),
        ([1], [1], {1}),
        ([1, 2, 3, 4], [2, 4], {2, 4}),
        ([], [], set()),
        ([5, 6], [6, 7, 8], {6}),
        ([1, 2], [2, 1], {1, 2}),
    ],
)
def test_common_elements(a, b, expected):
    assert common_elements(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([1, 2, 3], [2, 3, 4], {1}),
        ([1, 2], [1, 2], set()),
        ([1, 2, 3], [], {1, 2, 3}),
        ([], [1, 2], set()),
        (["a", "b", "c"], ["b"], {"a", "c"}),
        ([1], [2], {1}),
        ([1, 2, 3, 4], [1, 3], {2, 4}),
        ([5, 6], [5, 6], set()),
        ([1, 2, 2, 3], [2], {1, 3}),
        ([0], [1], {0}),
    ],
)
def test_only_in_first(a, b, expected):
    assert only_in_first(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([1, 2], [1, 2, 3], True),
        ([1, 5], [1, 2, 3], False),
        ([], [1, 2], True),
        ([1, 2, 3], [1, 2, 3], True),
        (["a"], ["a", "b"], True),
        ([1, 2], [2, 3], False),
        ([], [], True),
        ([1], [1], True),
        ([1, 2, 3], [1, 2], False),
        ([4], [1, 2, 3], False),
    ],
)
def test_is_subset(a, b, expected):
    assert is_subset(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([1, 2, 3], [2, 3, 4], {1, 4}),
        ([1, 2], [1, 2], set()),
        ([], [1, 2], {1, 2}),
        ([1, 2, 3], [], {1, 2, 3}),
        (["a", "b"], ["b", "c"], {"a", "c"}),
        ([1], [2], {1, 2}),
        ([1, 2], [3, 4], {1, 2, 3, 4}),
        ([5, 6, 7], [6, 7, 8], {5, 8}),
        ([1], [1], set()),
        ([1, 2, 3], [4, 5, 6], {1, 2, 3, 4, 5, 6}),
    ],
)
def test_symmetric_difference_manual(a, b, expected):
    assert symmetric_difference_manual(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([1, 2], [3, 4], True),
        ([1, 2], [2, 3], False),
        ([], [1], True),
        ([1], [1], False),
        (["a"], ["b"], True),
        ([], [], True),
        ([1, 2, 3], [4, 5, 6], True),
        ([1, 2, 3], [3, 4, 5], False),
        ([0], [0], False),
        ([1, 2], [], True),
    ],
)
def test_is_disjoint(a, b, expected):
    assert is_disjoint(a, b) == expected
