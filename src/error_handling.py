"""Exercises: Error Handling (try/except/else/finally, raise, assert)."""


def safe_int(s: str):
    """Try to convert s to int using try/except. Return the int on success,
    or None if a ValueError is raised.

    >>> safe_int("42")
    42
    >>> safe_int("nope") is None
    True
    """
    raise NotImplementedError("TODO: implement safe_int")


class NegativeValueError(Exception):
    """Custom exception for when a negative value isn't allowed."""


def require_non_negative(n: float) -> float:
    """Return n if n >= 0, otherwise raise NegativeValueError(...) with a
    message. Use `raise`.

    >>> require_non_negative(5)
    5
    """
    raise NotImplementedError("TODO: implement require_non_negative")


def divide_with_report(a: float, b: float) -> str:
    """Try to compute a / b.
    - If it raises ZeroDivisionError, return "Cannot divide by zero!"
    - Otherwise (else branch), return f"Result: {result}"
    - Either way (finally branch), doesn't matter what. Just make sure the
      try/except/else you write actually uses all three: try, except, else.

    >>> divide_with_report(10, 2)
    'Result: 5.0'
    >>> divide_with_report(10, 0)
    'Cannot divide by zero!'
    """
    raise NotImplementedError("TODO: implement divide_with_report")


def validate_age(age: int) -> int:
    """Use `assert` to check that age is between 0 and 150 (inclusive).
    If the assertion passes, return age unchanged.

    >>> validate_age(25)
    25
    """
    raise NotImplementedError("TODO: implement validate_age")


def retry(func, attempts: int = 3):
    """Call func() (no arguments). If it raises an exception, call it again,
    up to `attempts` total tries. Return the result of the first call that
    succeeds. If every attempt fails, re-raise the exception from the last
    attempt.

    >>> tries = []
    >>> def flaky():
    ...     tries.append(1)
    ...     if len(tries) < 2:
    ...         raise ValueError("not yet")
    ...     return "ok"
    >>> retry(flaky, attempts=3)
    'ok'
    """
    raise NotImplementedError("TODO: implement retry")


def validate_password(password: str) -> str:
    """Check password against three rules, in this order, raising
    ValueError with a specific message for the first one it violates:
      - fewer than 8 characters -> "password must be at least 8 characters long"
      - no digit anywhere       -> "password must contain at least one digit"
      - no uppercase letter     -> "password must contain at least one uppercase letter"
    If all rules pass, return password unchanged.

    >>> validate_password("Valid1Password")
    'Valid1Password'
    """
    raise NotImplementedError("TODO: implement validate_password")
