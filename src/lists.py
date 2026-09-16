"""Exercises: Lists."""


def add_item(items: list, item) -> list:
    """Append item to the end of items and return the list.

    >>> add_item([1, 2], 3)
    [1, 2, 3]
    """
    raise NotImplementedError("TODO: implement add_item")


def remove_duplicates(items: list) -> list:
    """Return a new list with duplicates removed, preserving the original
    order of first appearance. Do NOT just use set(items): that loses order.

    >>> remove_duplicates([1, 2, 2, 3, 1, 4])
    [1, 2, 3, 4]
    """
    raise NotImplementedError("TODO: implement remove_duplicates")


def second_largest(numbers: list) -> int:
    """Return the second-largest distinct value in numbers.

    >>> second_largest([3, 1, 4, 1, 5, 9])
    5
    """
    raise NotImplementedError("TODO: implement second_largest")


def flatten(nested: list) -> list:
    """Flatten a list that is one level nested (a list of lists) into a
    single flat list.

    >>> flatten([[1, 2], [3], [4, 5, 6]])
    [1, 2, 3, 4, 5, 6]
    """
    raise NotImplementedError("TODO: implement flatten")


def chunk(items: list, size: int) -> list:
    """Split items into consecutive chunks of length `size` (the last chunk
    may be shorter).

    >>> chunk([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    """
    raise NotImplementedError("TODO: implement chunk")


def rotate(items: list, n: int) -> list:
    """Return a new list with items rotated left by n positions (the
    first n items move to the end). n may be larger than len(items) or
    negative; handle both.

    >>> rotate([1, 2, 3, 4, 5], 2)
    [3, 4, 5, 1, 2]
    >>> rotate([1, 2, 3], -1)
    [3, 1, 2]
    """
    raise NotImplementedError("TODO: implement rotate")


def merge_sorted(a: list, b: list) -> list:
    """a and b are already sorted in ascending order. Return a single
    sorted list containing all their elements, without calling sorted()
    or .sort(): merge them yourself in one pass.

    >>> merge_sorted([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    """
    raise NotImplementedError("TODO: implement merge_sorted")
