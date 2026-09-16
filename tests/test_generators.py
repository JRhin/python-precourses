import inspect

import pytest

from src.generators import countdown, even_numbers, fibonacci, sliding_window, squares_generator_expr, take


@pytest.mark.parametrize(
    "n, expected",
    [
        (3, [3, 2, 1]),
        (1, [1]),
        (0, []),
        (5, [5, 4, 3, 2, 1]),
        (2, [2, 1]),
        (4, [4, 3, 2, 1]),
        (10, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
        (6, [6, 5, 4, 3, 2, 1]),
        (7, [7, 6, 5, 4, 3, 2, 1]),
        (8, [8, 7, 6, 5, 4, 3, 2, 1]),
    ],
)
def test_countdown(n, expected):
    result = countdown(n)
    assert inspect.isgenerator(result)
    assert list(result) == expected


@pytest.mark.parametrize(
    "limit, expected",
    [
        (10, [0, 2, 4, 6, 8]),
        (0, []),
        (1, [0]),
        (5, [0, 2, 4]),
        (20, [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]),
        (2, [0]),
        (4, [0, 2]),
        (12, [0, 2, 4, 6, 8, 10]),
        (15, [0, 2, 4, 6, 8, 10, 12, 14]),
        (6, [0, 2, 4]),
    ],
)
def test_even_numbers(limit, expected):
    assert list(even_numbers(limit)) == expected


@pytest.mark.parametrize(
    "count, expected",
    [
        (6, [0, 1, 1, 2, 3, 5]),
        (1, [0]),
        (0, []),
        (2, [0, 1]),
        (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
        (3, [0, 1, 1]),
        (4, [0, 1, 1, 2]),
        (5, [0, 1, 1, 2, 3]),
        (7, [0, 1, 1, 2, 3, 5, 8]),
        (8, [0, 1, 1, 2, 3, 5, 8, 13]),
    ],
)
def test_fibonacci(count, expected):
    assert list(fibonacci(count)) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (4, [0, 1, 4, 9]),
        (0, []),
        (1, [0]),
        (3, [0, 1, 4]),
        (10, [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]),
        (2, [0, 1]),
        (5, [0, 1, 4, 9, 16]),
        (6, [0, 1, 4, 9, 16, 25]),
        (7, [0, 1, 4, 9, 16, 25, 36]),
        (8, [0, 1, 4, 9, 16, 25, 36, 49]),
    ],
)
def test_squares_generator_expr(n, expected):
    result = squares_generator_expr(n)
    assert not isinstance(result, list)
    assert list(result) == expected


@pytest.mark.parametrize(
    "iterable, size, expected",
    [
        ([1, 2, 3, 4], 2, [(1, 2), (2, 3), (3, 4)]),
        ([1, 2, 3, 4, 5], 3, [(1, 2, 3), (2, 3, 4), (3, 4, 5)]),
        ([1, 2], 2, [(1, 2)]),
        ([1, 2, 3], 1, [(1,), (2,), (3,)]),
        (range(0, 5), 2, [(0, 1), (1, 2), (2, 3), (3, 4)]),
        ([1, 2, 3, 4, 5, 6], 4, [(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)]),
        (["a", "b", "c"], 2, [("a", "b"), ("b", "c")]),
        ([1, 2], 1, [(1,), (2,)]),
        (range(0, 6), 3, [(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 5)]),
        ([5, 4, 3, 2, 1], 2, [(5, 4), (4, 3), (3, 2), (2, 1)]),
    ],
)
def test_sliding_window(iterable, size, expected):
    assert list(sliding_window(iterable, size)) == expected


@pytest.mark.parametrize(
    "iterable, n, expected",
    [
        ([1, 2, 3, 4, 5], 2, [1, 2]),
        ([1, 2, 3], 0, []),
        ([1, 2, 3], 10, [1, 2, 3]),
        (range(0, 100), 3, [0, 1, 2]),
        ("abcdef", 3, ["a", "b", "c"]),
        ([1, 2, 3, 4], 1, [1]),
        ([], 5, []),
        ([9, 8, 7], 2, [9, 8]),
        (range(0, 3), 3, [0, 1, 2]),
        ("xy", 1, ["x"]),
    ],
)
def test_take(iterable, n, expected):
    assert list(take(iterable, n)) == expected


def _naturals():
    i = 0
    while True:
        yield i
        i += 1


def test_take_stops_early_on_infinite_iterable():
    assert list(take(_naturals(), 5)) == [0, 1, 2, 3, 4]


def test_take_does_not_over_consume():
    gen = _naturals()
    assert list(take(gen, 3)) == [0, 1, 2]
    assert next(gen) == 3
