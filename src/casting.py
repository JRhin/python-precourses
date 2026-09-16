"""Exercises: Casting."""


def to_int_safe(s: str, default: int = 0) -> int:
    """Try to cast s to int. If it fails, return default instead.

    >>> to_int_safe("42")
    42
    >>> to_int_safe("not a number", default=-1)
    -1
    """
    raise NotImplementedError("TODO: implement to_int_safe")


def celsius_to_fahrenheit(celsius: str) -> float:
    """celsius arrives as a string (e.g. from input()). Convert it to a
    Fahrenheit float ( F = C * 9/5 + 32 ).

    >>> celsius_to_fahrenheit("0")
    32.0
    >>> celsius_to_fahrenheit("100")
    212.0
    """
    raise NotImplementedError("TODO: implement celsius_to_fahrenheit")


def parse_bool(s: str) -> bool:
    """Convert a string like "true"/"True"/"false"/"False" (any case) to a
    real bool. Do NOT just use bool(s): bool("False") is True in Python!

    >>> parse_bool("true")
    True
    >>> parse_bool("False")
    False
    """
    raise NotImplementedError("TODO: implement parse_bool")


def parse_csv_row(row: str) -> list:
    """row is a comma-separated string of mixed values, e.g. "1,2.5,hello".
    Split it and cast each piece to the most specific type that fits: int
    if possible, otherwise float if possible, otherwise leave it as a
    (stripped) string.

    >>> parse_csv_row("1,2.5,hello")
    [1, 2.5, 'hello']
    >>> parse_csv_row("a,b,c")
    ['a', 'b', 'c']
    """
    raise NotImplementedError("TODO: implement parse_csv_row")


def safe_cast_all(values: list, target_type) -> list:
    """Try to cast every item in values to target_type (e.g. int, float,
    str, bool). Skip (omit) any item that can't be cast, instead of
    raising.

    >>> safe_cast_all(["1", "2", "x"], int)
    [1, 2]
    >>> safe_cast_all([1, 2, 3], str)
    ['1', '2', '3']
    """
    raise NotImplementedError("TODO: implement safe_cast_all")
