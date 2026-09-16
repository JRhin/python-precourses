"""Exercises: Lambda Functions."""


def sort_by_length(words: list) -> list:
    """Return words sorted from shortest to longest, using sorted() with a
    lambda as the `key`.

    >>> sort_by_length(["banana", "kiwi", "fig"])
    ['fig', 'kiwi', 'banana']
    """
    raise NotImplementedError("TODO: implement sort_by_length")


def square_all(numbers: list) -> list:
    """Return a list with every number squared, using map() with a lambda.

    >>> square_all([1, 2, 3, 4])
    [1, 4, 9, 16]
    """
    raise NotImplementedError("TODO: implement square_all")


def keep_positive(numbers: list) -> list:
    """Return only the positive numbers, using filter() with a lambda.

    >>> keep_positive([-2, -1, 0, 1, 2])
    [1, 2]
    """
    raise NotImplementedError("TODO: implement keep_positive")


def build_adder(n: int):
    """Return a lambda (assigned to a variable, that's fine) that takes one
    argument x and returns x + n.

    >>> add5 = build_adder(5)
    >>> add5(10)
    15
    """
    raise NotImplementedError("TODO: implement build_adder")


def sort_by_multiple_keys(people: list) -> list:
    """people is a list of (name, age) tuples. Return them sorted primarily
    by age (ascending), and by name (alphabetically) to break ties, using
    sorted() with a lambda key that returns a tuple.

    >>> sort_by_multiple_keys([("Bob", 30), ("Alice", 25), ("Zoe", 25)])
    [('Alice', 25), ('Zoe', 25), ('Bob', 30)]
    """
    raise NotImplementedError("TODO: implement sort_by_multiple_keys")


def reduce_product(numbers: list) -> int:
    """Return the product of all numbers in the (non-empty) list, using
    functools.reduce with a lambda. Do NOT use a loop or math.prod.

    >>> reduce_product([1, 2, 3, 4])
    24
    """
    raise NotImplementedError("TODO: implement reduce_product")
