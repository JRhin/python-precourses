"""Exercises: Functions (scope, nested functions, defaults)."""


def safe_divide(a: float, b: float, default: float = 0.0) -> float:
    """Return a / b, or `default` if b is 0. Use a plain if, not try/except.

    >>> safe_divide(10, 2)
    5.0
    >>> safe_divide(10, 0, default=-1)
    -1
    """
    raise NotImplementedError("TODO: implement safe_divide")


def apply_twice(f, x):
    """Call f on x, then call f again on the result, and return that.

    >>> apply_twice(lambda n: n * 2, 3)
    12
    """
    raise NotImplementedError("TODO: implement apply_twice")


def make_counter():
    """Return a function with no arguments that, every time it's called,
    returns the next integer starting from 1 (1, 2, 3, ...). Use a nested
    function and a variable captured from the enclosing scope (`nonlocal`).

    >>> counter = make_counter()
    >>> counter()
    1
    >>> counter()
    2
    >>> counter2 = make_counter()  # a fresh, independent counter
    >>> counter2()
    1
    """
    raise NotImplementedError("TODO: implement make_counter")


def make_multiplier(factor: int):
    """Return a function of one argument x that returns x * factor.

    >>> triple = make_multiplier(3)
    >>> triple(5)
    15
    """
    raise NotImplementedError("TODO: implement make_multiplier")


def memoize(f):
    """Return a wrapped version of f (which takes one argument) that
    caches results: the second time it's called with an argument it has
    already seen, it returns the cached result instead of calling f again.

    >>> calls = []
    >>> def slow_square(n):
    ...     calls.append(n)
    ...     return n * n
    >>> fast_square = memoize(slow_square)
    >>> fast_square(4)
    16
    >>> fast_square(4)
    16
    >>> calls
    [4]
    """
    raise NotImplementedError("TODO: implement memoize")


def compose(*funcs):
    """Return a new function that applies the given functions right to
    left: compose(f, g, h)(x) is equivalent to f(g(h(x))).

    >>> add_one = lambda x: x + 1
    >>> double = lambda x: x * 2
    >>> compose(double, add_one)(3)
    8
    """
    raise NotImplementedError("TODO: implement compose")
