import pytest

from src.loops import (
    factorial,
    filter_even,
    find_first_multiple,
    flatten_deep,
    moving_average,
    pair_names_ages,
    squares_comprehension,
    sum_up_to,
)


@pytest.mark.parametrize(
    "n, expected",
    [(5, 15), (1, 1), (0, 0), (10, 55), (100, 5050), (2, 3), (3, 6), (20, 210), (50, 1275), (7, 28)],
)
def test_sum_up_to(n, expected):
    assert sum_up_to(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [(5, 120), (0, 1), (1, 1), (3, 6), (6, 720), (10, 3628800), (2, 2), (7, 5040), (4, 24), (8, 40320)],
)
def test_factorial(n, expected):
    assert factorial(n) == expected


@pytest.mark.parametrize(
    "numbers, divisor, expected",
    [
        ([1, 3, 7, 8, 9], 4, 8),
        ([1, 2, 3], 5, None),
        ([2, 4, 6], 2, 2),
        ([1, 3, 5], 2, None),
        ([10, 15, 20], 5, 10),
        ([7], 7, 7),
        ([1, 2, 3, 4], 3, 3),
        ([9, 18, 27], 9, 9),
        ([1, 1, 1], 1, 1),
        ([2, 3, 5, 7], 7, 7),
    ],
)
def test_find_first_multiple(numbers, divisor, expected):
    assert find_first_multiple(numbers, divisor) == expected


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3, 4, 5, 6], [2, 4, 6]),
        ([], []),
        ([1, 3, 5], []),
        ([2, 4, 6], [2, 4, 6]),
        ([0, 1, 2], [0, 2]),
        ([-2, -1, 0, 1, 2], [-2, 0, 2]),
        ([7], []),
        ([10, 11, 12, 13], [10, 12]),
        ([1], []),
        ([2], [2]),
    ],
)
def test_filter_even(numbers, expected):
    assert filter_even(numbers) == expected


@pytest.mark.parametrize(
    "names, ages, expected",
    [
        (["Pippo", "Bob"], [25, 30], [("Pippo", 25), ("Bob", 30)]),
        ([], [], []),
        (["A"], [1], [("A", 1)]),
        (["X", "Y", "Z"], [1, 2, 3], [("X", 1), ("Y", 2), ("Z", 3)]),
        (["a", "b"], [10, 20], [("a", 10), ("b", 20)]),
        (["one"], [1], [("one", 1)]),
        (["m", "n", "o"], [5, 6, 7], [("m", 5), ("n", 6), ("o", 7)]),
        (["p"], [100], [("p", 100)]),
        (["q", "r"], [0, 0], [("q", 0), ("r", 0)]),
        (["s", "t", "u"], [1, 1, 1], [("s", 1), ("t", 1), ("u", 1)]),
    ],
)
def test_pair_names_ages(names, ages, expected):
    assert pair_names_ages(names, ages) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, [0, 1, 4, 9, 16]),
        (0, []),
        (1, [0]),
        (3, [0, 1, 4]),
        (10, [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]),
        (2, [0, 1]),
        (4, [0, 1, 4, 9]),
        (6, [0, 1, 4, 9, 16, 25]),
        (7, [0, 1, 4, 9, 16, 25, 36]),
        (8, [0, 1, 4, 9, 16, 25, 36, 49]),
    ],
)
def test_squares_comprehension(n, expected):
    assert squares_comprehension(n) == expected


@pytest.mark.parametrize(
    "nested, expected",
    [
        ([1, [2, 3], [4, [5, 6]]], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3], [1, 2, 3]),
        ([[1, [2, [3, [4]]]]], [1, 2, 3, 4]),
        ([], []),
        ([1, [2, [3, [4, [5]]]]], [1, 2, 3, 4, 5]),
        ([[1], [2], [3]], [1, 2, 3]),
        ([1, [2], 3, [4, [5]]], [1, 2, 3, 4, 5]),
        ([[[1, 2], [3]], 4], [1, 2, 3, 4]),
        ([1], [1]),
        ([[[[1]]]], [1]),
    ],
)
def test_flatten_deep(nested, expected):
    assert flatten_deep(nested) == expected


@pytest.mark.parametrize(
    "numbers, window, expected",
    [
        ([1, 2, 3, 4, 5], 2, [1.5, 2.5, 3.5, 4.5]),
        ([1, 2, 3, 4, 5], 1, [1.0, 2.0, 3.0, 4.0, 5.0]),
        ([1, 2, 3, 4, 5], 5, [3.0]),
        ([2, 4, 6, 8], 2, [3.0, 5.0, 7.0]),
        ([1, 1, 1, 1], 2, [1.0, 1.0, 1.0]),
        ([10, 20, 30], 3, [20.0]),
        ([1, 2, 3], 2, [1.5, 2.5]),
        ([5, 10, 15, 20, 25], 3, [10.0, 15.0, 20.0]),
        ([0, 0, 0], 1, [0.0, 0.0, 0.0]),
        ([1, 3, 5, 7, 9], 2, [2.0, 4.0, 6.0, 8.0]),
    ],
)
def test_moving_average(numbers, window, expected):
    assert moving_average(numbers, window) == expected
