import pytest

from src.functions import apply_twice, compose, make_counter, make_multiplier, memoize, safe_divide


@pytest.mark.parametrize(
    "a, b, default, expected",
    [
        (10, 2, 0.0, 5.0),
        (10, 0, -1, -1),
        (9, 3, 0.0, 3.0),
        (1, 0, None, None),
        (-10, 2, 0.0, -5.0),
        (0, 5, 0.0, 0.0),
        (7, 0, 0, 0),
        (5, 5, 0.0, 1.0),
        (10, 3, 0.0, pytest.approx(3.3333333333333335)),
        (-8, 0, -99, -99),
    ],
)
def test_safe_divide(a, b, default, expected):
    assert safe_divide(a, b, default) == expected


@pytest.mark.parametrize(
    "f, x, expected",
    [
        (lambda n: n * 2, 3, 12),
        (lambda n: n + 1, 0, 2),
        (lambda n: n**2, 2, 16),
        (lambda s: s + "!", "hi", "hi!!"),
        (lambda n: n - 1, 10, 8),
        (lambda n: n / 2, 8, 2.0),
        (lambda s: s.upper(), "go", "GO"),
        (lambda n: -n, 5, 5),
        (lambda n: n * n * n, 2, 512),
        (lambda lst: lst + [1], [], [1, 1]),
    ],
)
def test_apply_twice(f, x, expected):
    assert apply_twice(f, x) == expected


@pytest.mark.parametrize("n_calls", range(1, 11))
def test_make_counter(n_calls):
    counter = make_counter()
    results = [counter() for _ in range(n_calls)]
    assert results == list(range(1, n_calls + 1))


def test_make_counter_independent_instances():
    counter1 = make_counter()
    counter2 = make_counter()
    assert counter1() == 1
    assert counter1() == 2
    assert counter2() == 1
    assert counter1() == 3
    assert counter2() == 2


@pytest.mark.parametrize(
    "factor, x, expected",
    [(3, 5, 15), (0, 100, 0), (-2, 4, -8), (1, 7, 7), (10, -3, -30), (5, 0, 0), (2, 2, 4), (-1, -1, 1), (100, 1, 100), (7, 3, 21)],
)
def test_make_multiplier(factor, x, expected):
    assert make_multiplier(factor)(x) == expected


@pytest.mark.parametrize(
    "calls, expected_results, expected_calls_made",
    [
        ([5, 5], [25, 25], [5]),
        ([1, 2, 1, 2], [1, 4, 1, 4], [1, 2]),
        ([3], [9], [3]),
        ([0, 0, 0], [0, 0, 0], [0]),
        ([2, 3, 2, 3, 2], [4, 9, 4, 9, 4], [2, 3]),
        ([7, 7, 7, 7], [49, 49, 49, 49], [7]),
        ([-1, -1], [1, 1], [-1]),
        ([4, 5, 6], [16, 25, 36], [4, 5, 6]),
        ([10, 10, 20, 10], [100, 100, 400, 100], [10, 20]),
        ([1], [1], [1]),
    ],
)
def test_memoize(calls, expected_results, expected_calls_made):
    calls_made = []

    def square(n):
        calls_made.append(n)
        return n * n

    fast_square = memoize(square)
    results = [fast_square(n) for n in calls]
    assert results == expected_results
    assert calls_made == expected_calls_made


def _add1(x):
    return x + 1


def _double(x):
    return x * 2


def _square(x):
    return x * x


def _neg(x):
    return -x


def _inc10(x):
    return x + 10


@pytest.mark.parametrize(
    "funcs, x, expected",
    [
        ((_double, _add1), 3, 8),
        ((_add1, _double), 3, 7),
        ((_square, _add1), 2, 9),
        ((_neg, _double), 5, -10),
        ((_double, _double, _double), 1, 8),
        ((_add1, _add1, _add1), 0, 3),
        ((_square, _double), 3, 36),
        ((_double, _square), 3, 18),
        ((_neg, _add1, _double), 2, -5),
        ((_inc10,), 5, 15),
    ],
)
def test_compose(funcs, x, expected):
    assert compose(*funcs)(x) == expected
