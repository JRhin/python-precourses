"""Exercises: Variables & Types."""


def get_type_name(value) -> str:
    """Return the name of ``value``'s type as a string.

    >>> get_type_name(10)
    'int'
    >>> get_type_name("hi")
    'str'
    """
    raise NotImplementedError("TODO: implement get_type_name")


def swap_values(a, b) -> tuple:
    """Return a tuple with ``a`` and ``b`` swapped.

    >>> swap_values(1, 2)
    (2, 1)
    """
    raise NotImplementedError("TODO: implement swap_values")


def describe_person(name: str, age: int, height_in_m: float, is_student: bool) -> str:
    """Return a one-line description of a person, combining the four
    values below into a single sentence. Study the examples carefully to
    figure out the exact wording, punctuation, and spacing.

    >>> describe_person("Pippo", 25, 1.75, True)
    'Pippo is 25 years old, 1.75m tall, and is a student: True.'
    >>> describe_person("Anna", 30, 1.6, False)
    'Anna is 30 years old, 1.6m tall, and is a student: False.'
    """
    raise NotImplementedError("TODO: implement describe_person")


def is_same_type(a, b) -> bool:
    """Return True if a and b have exactly the same type. Careful: in
    Python, `bool` is technically a subclass of `int`, so `1` and `True`
    should NOT count as the same type here.

    >>> is_same_type(1, 2)
    True
    >>> is_same_type(1, True)
    False
    """
    raise NotImplementedError("TODO: implement is_same_type")


def most_common_type(values: list) -> str:
    """Given a list of mixed values, return the name of the type that
    appears most often (e.g. "int", "str", "list", ...). Assume there's no
    tie in the inputs you're tested against.

    >>> most_common_type([1, 2, "a"])
    'int'
    >>> most_common_type(["a", "b", 1])
    'str'
    """
    raise NotImplementedError("TODO: implement most_common_type")
