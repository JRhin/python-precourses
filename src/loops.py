"""Exercises: Loops & Iterations."""


def sum_up_to(n: int) -> int:
    """Return 1 + 2 + ... + n using a while loop (not the sum()/formula
    shortcut).

    >>> sum_up_to(5)
    15
    """
    raise NotImplementedError("TODO: implement sum_up_to")


def factorial(n: int) -> int:
    """Return n! (n factorial) using a for loop.

    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    raise NotImplementedError("TODO: implement factorial")


def find_first_multiple(numbers: list, divisor: int):
    """Return the first number in `numbers` that is a multiple of `divisor`,
    using a for loop with `break`. Return None if there isn't one.

    >>> find_first_multiple([1, 3, 7, 8, 9], 4)
    8
    """
    raise NotImplementedError("TODO: implement find_first_multiple")


def filter_even(numbers: list) -> list:
    """Return only the even numbers from `numbers`, using a for loop with
    `continue` to skip odd ones (not a list comprehension).

    >>> filter_even([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    """
    raise NotImplementedError("TODO: implement filter_even")


def pair_names_ages(names: list, ages: list) -> list:
    """Use zip() to combine names and ages into a list of (name, age) tuples.

    >>> pair_names_ages(["Pippo", "Bob"], [25, 30])
    [('Pippo', 25), ('Bob', 30)]
    """
    raise NotImplementedError("TODO: implement pair_names_ages")


def squares_comprehension(n: int) -> list:
    """Return [0**2, 1**2, ..., (n-1)**2] using a list comprehension.

    >>> squares_comprehension(5)
    [0, 1, 4, 9, 16]
    """
    raise NotImplementedError("TODO: implement squares_comprehension")


def flatten_deep(nested: list) -> list:
    """nested is a list that may contain ints and/or other lists, nested
    to any depth. Return a single flat list of all the ints, in order.

    >>> flatten_deep([1, [2, 3], [4, [5, 6]]])
    [1, 2, 3, 4, 5, 6]
    """
    raise NotImplementedError("TODO: implement flatten_deep")


def moving_average(numbers: list, window: int) -> list:
    """Return the moving average of numbers using a window of size
    `window`: result[i] is the average of numbers[i : i + window]. The
    result has len(numbers) - window + 1 elements.

    >>> moving_average([1, 2, 3, 4, 5], 2)
    [1.5, 2.5, 3.5, 4.5]
    """
    raise NotImplementedError("TODO: implement moving_average")
