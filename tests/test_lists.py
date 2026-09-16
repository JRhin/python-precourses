import pytest

from src.lists import add_item, chunk, flatten, merge_sorted, remove_duplicates, rotate, second_largest


@pytest.mark.parametrize(
    "items, item, expected",
    [
        ([1, 2], 3, [1, 2, 3]),
        ([], 1, [1]),
        ([1], 2, [1, 2]),
        (["a"], "b", ["a", "b"]),
        ([1, 2, 3], 4, [1, 2, 3, 4]),
        ([], [1], [[1]]),
        ([0], 0, [0, 0]),
        ([1, 1], 1, [1, 1, 1]),
        (["x", "y"], "z", ["x", "y", "z"]),
        ([True], False, [True, False]),
    ],
)
def test_add_item(items, item, expected):
    assert add_item(items, item) == expected


@pytest.mark.parametrize(
    "items, expected",
    [
        ([1, 2, 2, 3, 1, 4], [1, 2, 3, 4]),
        ([], []),
        ([1, 1, 1], [1]),
        ([1, 2, 3], [1, 2, 3]),
        (["a", "b", "a"], ["a", "b"]),
        ([1, "1", 1], [1, "1"]),
        ([3, 2, 1, 2, 3], [3, 2, 1]),
        ([5], [5]),
        ([1, 2, 1, 2, 1], [1, 2]),
        ([0, 0, 1, 1, 0], [0, 1]),
    ],
)
def test_remove_duplicates(items, expected):
    assert remove_duplicates(items) == expected


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([3, 1, 4, 1, 5, 9], 5),
        ([1, 2], 1),
        ([5, 5, 4], 4),
        ([10, 20, 30], 20),
        ([-1, -2, -3], -2),
        ([0, 0, 1], 0),
        ([100, 99], 99),
        ([7, 3, 3, 7, 1], 3),
        ([2, 1], 1),
        ([1, 2, 3, 4, 5], 4),
    ],
)
def test_second_largest(numbers, expected):
    assert second_largest(numbers) == expected


@pytest.mark.parametrize(
    "nested, expected",
    [
        ([[1, 2], [3], [4, 5, 6]], [1, 2, 3, 4, 5, 6]),
        ([[1], [2], [3]], [1, 2, 3]),
        ([[], [1, 2]], [1, 2]),
        ([[1, 2, 3]], [1, 2, 3]),
        ([[], []], []),
        ([[1], [], [2, 3]], [1, 2, 3]),
        ([["a"], ["b", "c"]], ["a", "b", "c"]),
        ([[1, 2], [3, 4], [5, 6]], [1, 2, 3, 4, 5, 6]),
        ([[0]], [0]),
        ([[1], [2], [3], [4]], [1, 2, 3, 4]),
    ],
)
def test_flatten(nested, expected):
    assert flatten(nested) == expected


@pytest.mark.parametrize(
    "items, size, expected",
    [
        ([1, 2, 3, 4, 5], 2, [[1, 2], [3, 4], [5]]),
        ([1, 2, 3, 4], 2, [[1, 2], [3, 4]]),
        ([1, 2, 3], 1, [[1], [2], [3]]),
        ([1, 2, 3, 4, 5, 6], 3, [[1, 2, 3], [4, 5, 6]]),
        ([1], 5, [[1]]),
        ([], 3, []),
        ([1, 2, 3, 4, 5], 10, [[1, 2, 3, 4, 5]]),
        ([0, 1, 2, 3, 4, 5, 6], 3, [[0, 1, 2], [3, 4, 5], [6]]),
        ([1, 2], 2, [[1, 2]]),
        (list(range(10)), 4, [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]),
    ],
)
def test_chunk(items, size, expected):
    assert chunk(items, size) == expected


@pytest.mark.parametrize(
    "items, n, expected",
    [
        ([1, 2, 3, 4, 5], 2, [3, 4, 5, 1, 2]),
        ([1, 2, 3], 1, [2, 3, 1]),
        ([1, 2, 3], 0, [1, 2, 3]),
        ([1, 2, 3], 3, [1, 2, 3]),
        ([1, 2, 3], 4, [2, 3, 1]),
        ([1, 2, 3], -1, [3, 1, 2]),
        ([], 2, []),
        ([1], 5, [1]),
        ([1, 2, 3, 4], 2, [3, 4, 1, 2]),
        ([1, 2, 3, 4, 5], 7, [3, 4, 5, 1, 2]),
    ],
)
def test_rotate(items, n, expected):
    assert rotate(items, n) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2], [3, 4], [1, 2, 3, 4]),
        ([], [1, 2], [1, 2]),
        ([1, 2], [], [1, 2]),
        ([1, 1, 2], [1, 2, 2], [1, 1, 1, 2, 2, 2]),
        ([5], [1], [1, 5]),
        ([1, 2, 3], [1, 2, 3], [1, 1, 2, 2, 3, 3]),
        ([-3, -1], [-2, 0], [-3, -2, -1, 0]),
        ([2, 4, 6], [1, 3, 5, 7], [1, 2, 3, 4, 5, 6, 7]),
        ([], [], []),
    ],
)
def test_merge_sorted(a, b, expected):
    assert merge_sorted(a, b) == expected
