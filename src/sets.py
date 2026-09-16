"""Exercises: Sets."""


def unique_elements(items: list) -> set:
    """Return the unique elements of items as a set.

    >>> unique_elements([1, 2, 2, 3]) == {1, 2, 3}
    True
    """
    raise NotImplementedError("TODO: implement unique_elements")


def common_elements(a: list, b: list) -> set:
    """Return the elements that appear in both a and b.

    >>> common_elements([1, 2, 3], [2, 3, 4]) == {2, 3}
    True
    """
    raise NotImplementedError("TODO: implement common_elements")


def only_in_first(a: list, b: list) -> set:
    """Return the elements that are in a but not in b.

    >>> only_in_first([1, 2, 3], [2, 3, 4]) == {1}
    True
    """
    raise NotImplementedError("TODO: implement only_in_first")


def is_subset(a: list, b: list) -> bool:
    """Return True if every element of a is also in b.

    >>> is_subset([1, 2], [1, 2, 3])
    True
    >>> is_subset([1, 5], [1, 2, 3])
    False
    """
    raise NotImplementedError("TODO: implement is_subset")


def symmetric_difference_manual(a: list, b: list) -> set:
    """Return the elements that are in exactly one of a, b (not both),
    without using the ^ operator.

    >>> symmetric_difference_manual([1, 2, 3], [2, 3, 4]) == {1, 4}
    True
    """
    raise NotImplementedError("TODO: implement symmetric_difference_manual")


def is_disjoint(a: list, b: list) -> bool:
    """Return True if a and b share no elements at all.

    >>> is_disjoint([1, 2], [3, 4])
    True
    >>> is_disjoint([1, 2], [2, 3])
    False
    """
    raise NotImplementedError("TODO: implement is_disjoint")
