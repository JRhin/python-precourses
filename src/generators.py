"""Exercises: Generators."""


def countdown(n: int):
    """A generator function: yield n, n-1, ..., down to 1 (inclusive).
    Use `yield`, not `return [...]`.

    >>> list(countdown(3))
    [3, 2, 1]
    """
    raise NotImplementedError("TODO: implement countdown")


def even_numbers(limit: int):
    """A generator function: yield the even numbers from 0 up to (but not
    including) `limit`.

    >>> list(even_numbers(10))
    [0, 2, 4, 6, 8]
    """
    raise NotImplementedError("TODO: implement even_numbers")


def fibonacci(count: int):
    """A generator function: yield the first `count` Fibonacci numbers,
    starting 0, 1, 1, 2, 3, 5, ...

    >>> list(fibonacci(6))
    [0, 1, 1, 2, 3, 5]
    """
    raise NotImplementedError("TODO: implement fibonacci")


def squares_generator_expr(n: int):
    """Return a generator (not a list!) of x**2 for x in range(n), using a
    generator expression (parentheses, not square brackets).

    >>> gen = squares_generator_expr(4)
    >>> list(gen)
    [0, 1, 4, 9]
    """
    raise NotImplementedError("TODO: implement squares_generator_expr")


def sliding_window(iterable, size: int):
    """A generator function: yield every consecutive window of `size`
    items from iterable, as tuples, sliding one item at a time.

    >>> list(sliding_window([1, 2, 3, 4], 2))
    [(1, 2), (2, 3), (3, 4)]
    """
    raise NotImplementedError("TODO: implement sliding_window")


def take(iterable, n: int):
    """A generator function: yield at most the first n items from
    iterable. If iterable has fewer than n items, stop early instead of
    raising an error. Must work on infinite iterables too (don't consume
    more than n items).

    >>> list(take([1, 2, 3, 4, 5], 2))
    [1, 2]
    >>> list(take([1, 2, 3], 10))
    [1, 2, 3]
    """
    raise NotImplementedError("TODO: implement take")
