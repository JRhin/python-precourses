"""Exercises: Tuples."""


def swap_tuple(t: tuple) -> tuple:
    """Given a 2-item tuple (a, b), return (b, a).

    >>> swap_tuple((1, 2))
    (2, 1)
    """
    raise NotImplementedError("TODO: implement swap_tuple")


def first_and_last(t: tuple) -> tuple:
    """Return a 2-tuple with the first and last elements of t.

    >>> first_and_last((10, 20, 30, 40))
    (10, 40)
    """
    raise NotImplementedError("TODO: implement first_and_last")


def pairs_to_dict(pairs: list) -> dict:
    """pairs is a list of (key, value) tuples. Return them as a dict.

    >>> pairs_to_dict([("a", 1), ("b", 2)])
    {'a': 1, 'b': 2}
    """
    raise NotImplementedError("TODO: implement pairs_to_dict")


def make_point(x: float, y: float) -> tuple:
    """Return an immutable (x, y) point as a tuple.

    >>> make_point(1, 2)
    (1, 2)
    """
    raise NotImplementedError("TODO: implement make_point")


def unzip(pairs: list) -> tuple:
    """The inverse of zip(): given a list of (a, b) tuples, return a
    2-tuple (list_of_as, list_of_bs).

    >>> unzip([(1, "a"), (2, "b"), (3, "c")])
    ([1, 2, 3], ['a', 'b', 'c'])
    """
    raise NotImplementedError("TODO: implement unzip")


def nested_tuple_sum(t: tuple) -> int:
    """t is a tuple that may contain ints and/or other tuples, nested to
    any depth. Return the sum of every int found anywhere inside it.

    >>> nested_tuple_sum((1, (2, 3), 4))
    10
    >>> nested_tuple_sum((1, (2, (3, 4))))
    10
    """
    raise NotImplementedError("TODO: implement nested_tuple_sum")
