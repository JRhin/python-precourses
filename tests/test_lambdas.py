import pytest

from src.lambdas import build_adder, keep_positive, reduce_product, sort_by_length, sort_by_multiple_keys, square_all


@pytest.mark.parametrize(
    "words, expected",
    [
        (["banana", "kiwi", "fig"], ["fig", "kiwi", "banana"]),
        (["a", "bb", "ccc"], ["a", "bb", "ccc"]),
        ([], []),
        (["same", "size"], ["same", "size"]),
        (["x"], ["x"]),
        (["ab", "a", "abc"], ["a", "ab", "abc"]),
        (["dog", "cat", "ox"], ["ox", "dog", "cat"]),
        (["longest", "short", "mid"], ["mid", "short", "longest"]),
        (["z", "yy", "xxx"], ["z", "yy", "xxx"]),
        (["one", "a", "three"], ["a", "one", "three"]),
    ],
)
def test_sort_by_length(words, expected):
    assert sort_by_length(words) == expected


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3, 4], [1, 4, 9, 16]),
        ([], []),
        ([0], [0]),
        ([-1, -2], [1, 4]),
        ([5], [25]),
        ([1, 1, 1], [1, 1, 1]),
        ([10, 20], [100, 400]),
        ([-3, 3], [9, 9]),
        ([2], [4]),
        ([0, 1, 2, 3], [0, 1, 4, 9]),
    ],
)
def test_square_all(numbers, expected):
    assert square_all(numbers) == expected


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([-2, -1, 0, 1, 2], [1, 2]),
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
        ([-1, -2, -3], []),
        ([0], []),
        ([5, -5], [5]),
        ([100], [100]),
        ([-100], []),
        ([1, -1, 2, -2], [1, 2]),
        ([0, 1, -1], [1]),
    ],
)
def test_keep_positive(numbers, expected):
    assert keep_positive(numbers) == expected


@pytest.mark.parametrize(
    "n, x, expected",
    [(5, 10, 15), (0, 5, 5), (-3, 3, 0), (10, -10, 0), (1, 1, 2), (100, 1, 101), (-5, -5, -10), (2, 2, 4), (0, 0, 0), (7, 7, 14)],
)
def test_build_adder(n, x, expected):
    assert build_adder(n)(x) == expected


@pytest.mark.parametrize(
    "people, expected",
    [
        ([("Bob", 30), ("Alice", 25), ("Zoe", 25)], [("Alice", 25), ("Zoe", 25), ("Bob", 30)]),
        ([("A", 1), ("B", 1), ("C", 1)], [("A", 1), ("B", 1), ("C", 1)]),
        ([], []),
        ([("X", 40)], [("X", 40)]),
        ([("Anna", 20), ("anna", 20)], [("Anna", 20), ("anna", 20)]),
        ([("B", 2), ("A", 1)], [("A", 1), ("B", 2)]),
        ([("C", 5), ("A", 5), ("B", 5)], [("A", 5), ("B", 5), ("C", 5)]),
        ([("Y", 1), ("X", 1)], [("X", 1), ("Y", 1)]),
        ([("Z", 10), ("A", 10), ("M", 5)], [("M", 5), ("A", 10), ("Z", 10)]),
        ([("A", 1), ("A", 2), ("A", 1)], [("A", 1), ("A", 1), ("A", 2)]),
    ],
)
def test_sort_by_multiple_keys(people, expected):
    assert sort_by_multiple_keys(people) == expected


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3, 4], 24),
        ([5], 5),
        ([2, 2, 2], 8),
        ([1, 1, 1], 1),
        ([3, 3], 9),
        ([10], 10),
        ([-1, 2, -3], 6),
        ([0, 5, 10], 0),
        ([6, 7], 42),
        ([1, 2, 3, 4, 5], 120),
    ],
)
def test_reduce_product(numbers, expected):
    assert reduce_product(numbers) == expected
