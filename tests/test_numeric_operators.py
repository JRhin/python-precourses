import pytest

from src.numeric_operators import average, divmod_pair, gcd_manual, is_even, is_prime, power


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (11, 5, (2, 1)),
        (10, 2, (5, 0)),
        (7, 3, (2, 1)),
        (20, 4, (5, 0)),
        (1, 1, (1, 0)),
        (0, 5, (0, 0)),
        (9, 9, (1, 0)),
        (15, 4, (3, 3)),
        (100, 7, (14, 2)),
        (5, 10, (0, 5)),
    ],
)
def test_divmod_pair(a, b, expected):
    assert divmod_pair(a, b) == expected


@pytest.mark.parametrize(
    "n, expected",
    [(4, True), (7, False), (0, True), (-2, True), (-3, False), (10, True), (1, False), (100, True), (99, False), (2, True)],
)
def test_is_even(n, expected):
    assert is_even(n) == expected


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3, 4], 2.5),
        ([5], 5.0),
        ([1, 1, 1], 1.0),
        ([-1, 0, 1], 0.0),
        ([2, 4, 6, 8, 10], 6.0),
        ([1.5, 2.5], 2.0),
        ([100], 100.0),
        ([0, 0, 0], 0.0),
        ([-5, -10], -7.5),
        ([3, 3, 3, 3], 3.0),
    ],
)
def test_average(numbers, expected):
    assert average(numbers) == expected


@pytest.mark.parametrize(
    "base, exponent, expected",
    [
        (2, 10, 1024),
        (3, 3, 27),
        (5, 0, 1),
        (2, 1, 2),
        (10, 2, 100),
        (1, 100, 1),
        (2, -1, 0.5),
        (4, 0.5, 2.0),
        (3, 4, 81),
        (0, 5, 0),
    ],
)
def test_power(base, exponent, expected):
    assert power(base, exponent) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (12, 8, 4),
        (17, 5, 1),
        (100, 75, 25),
        (0, 5, 5),
        (5, 0, 5),
        (21, 14, 7),
        (7, 7, 7),
        (48, 18, 6),
        (270, 192, 6),
        (1, 1, 1),
    ],
)
def test_gcd_manual(a, b, expected):
    assert gcd_manual(a, b) == expected


@pytest.mark.parametrize(
    "n, expected",
    [(2, True), (3, True), (4, False), (17, True), (18, False), (1, False), (0, False), (-5, False), (97, True), (100, False)],
)
def test_is_prime(n, expected):
    assert is_prime(n) == expected
