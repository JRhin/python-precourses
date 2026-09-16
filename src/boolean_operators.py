"""Exercises: Boolean Operators."""


def is_in_range(x: float, low: float, high: float) -> bool:
    """Return True if x is between low and high, inclusive on both ends.

    >>> is_in_range(5, 0, 10)
    True
    >>> is_in_range(-1, 0, 10)
    False
    """
    raise NotImplementedError("TODO: implement is_in_range")


def both_true(a: bool, b: bool) -> bool:
    """Return True only if both a and b are True.

    >>> both_true(True, True)
    True
    >>> both_true(True, False)
    False
    """
    raise NotImplementedError("TODO: implement both_true")


def either_true(a: bool, b: bool) -> bool:
    """Return True if at least one of a, b is True.

    >>> either_true(False, True)
    True
    >>> either_true(False, False)
    False
    """
    raise NotImplementedError("TODO: implement either_true")


def exactly_one(a: bool, b: bool) -> bool:
    """Return True if exactly one of a, b is True (and not both),
    without using the ^ operator.

    >>> exactly_one(True, False)
    True
    >>> exactly_one(True, True)
    False
    """
    raise NotImplementedError("TODO: implement exactly_one")


def majority_vote(a: bool, b: bool, c: bool) -> bool:
    """Return True if at least two of the three values are True.

    >>> majority_vote(True, True, False)
    True
    >>> majority_vote(True, False, False)
    False
    """
    raise NotImplementedError("TODO: implement majority_vote")


def implies(a: bool, b: bool) -> bool:
    """Return the logical implication "a implies b" (in formal logic,
    this is only False when a is True and b is False; every other
    combination is True).

    >>> implies(True, False)
    False
    >>> implies(False, False)
    True
    """
    raise NotImplementedError("TODO: implement implies")
